from flask_restx import Namespace, Resource, fields
from model.chapter import list_chapters, get_chapter, update_chapter
from model.choice import list_chapter_choices 
from model.item import list_items_received, list_required_items
from api.choice import choice
from api.receive import receive
from api.required import required

api = Namespace('Chapter', description='Gestion des chapitres d\'une histoire')

chapter = api.model('Chapter', {
    'id': fields.Integer(readonly=True, description="ID du chapitre"),
    'name': fields.String(required=True, description="Titre du chapitre"),
    'content': fields.String(required=True, description="Contenu du chapitre (markdown accepté)"),
    'story_id': fields.Integer(required=True, description="ID de l'histoire liée à ce chapitre"),
    'prev_choice_id': fields.Integer(readonly=True, description="ID du choix menant à ce chapitre"),
})

choice = api.inherit('ChoiceWithItems', choice, {
    'required_items': fields.List(fields.Nested(required), readonly=True, description="Liste des objets requis pour ce choix"),
})

chapter_detail = api.inherit('ChapterDetail', chapter, {
    'received_items': fields.List(fields.Nested(receive), readonly=True, description="Liste des objets reçus dans ce chapitre"),
    'choices': fields.List(fields.Nested(choice), readonly=True, description="Liste des choix disponibles dans ce chapitre"),
})

@api.route('/from_story/<int:story_id>', methods=["GET"])
class ChapterList(Resource):
    @api.marshal_with(chapter_detail)
    def get(self, story_id):
        chapters = list_chapters(story_id)

        for chapter in chapters:
            chapter['received_items'] = list_items_received(chapter['id'])
            choices = list_chapter_choices(chapter['id'])

            # Pour chaque choix, ajouter les objets requis
            for choice in choices:
                choice['required_items'] = list_required_items(choice['id'])

            chapter['choices'] = choices

        return chapters

@api.route('/<int:id>')
class ChapterDetail(Resource):
    @api.marshal_with(chapter_detail)
    def get(self, id):
        chapter = get_chapter(id)
        choices = list_chapter_choices(id)
        received_items = list_items_received(id)

        # Pour chaque choix, ajouter les objets requis
        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])

        # Ajouter les objets obtenus au chapitre
        chapter['received_items'] = received_items
        chapter['choices'] = choices

        return chapter
    
    @api.expect(chapter)
    @api.marshal_with(chapter)
    def put(self, id):
        data = api.payload
        update_chapter(id, data)
        return get_chapter(id)