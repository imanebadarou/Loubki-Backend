from flask_restx import Namespace, Resource, fields
from model.chapter import list_chapters, get_chapter
from model.choice import list_chapter_choices 
from model.item import list_items_received, list_required_items
from api.item import item
from api.choice import choice

api = Namespace('Chapter', description='Gestion des chapitres d\'une histoire')

chapter = api.model('Chapter', {
    'id': fields.Integer,
    'name': fields.String,
    'content': fields.String,
    'story_id': fields.Integer,
    'prev_choice_id': fields.Integer,
})

itemTransfer = api.inherit('ItemTransfer', item, {
    'quantity': fields.Integer,
    'name': fields.String,
})

choice = api.inherit('Choice', choice, {
    'required_items': fields.List(fields.Nested(itemTransfer)),
})

chapter_detail = api.inherit('ChapterDetail', chapter, {
    'received_items': fields.List(fields.Nested(itemTransfer)),
    'choices': fields.List(fields.Nested(choice)),
})

@api.route('/from_story/<int:key>', methods=["GET"])
class ChapterList(Resource):
    @api.marshal_with(chapter)
    def get(self, key):
        return list_chapters(key)

@api.route('/<int:chapter_id>', methods=["GET"])
class ChapterDetail(Resource):
    @api.marshal_with(chapter_detail)
    def get(self, chapter_id):
        chapter = get_chapter(chapter_id)
        choices = list_chapter_choices(chapter_id)
        received_items = list_items_received(chapter_id)

        # Pour chaque choix, ajouter les objets requis
        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])

        # Ajouter les objets obtenus au chapitre
        chapter['received_items'] = received_items
        chapter['choices'] = choices

        return chapter