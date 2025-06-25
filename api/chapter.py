from flask_restx import Namespace, Resource, fields
from model.chapter import list_chapters, get_chapter
from model.choice import list_chapter_choices 
from model.item import list_items_received, list_required_items

api = Namespace('Chapter', description='Gestion des chapitres d\'une histoire')

chapitre = api.model('Chapter', {
    'id': fields.Integer,
    'name': fields.String,
    'content': fields.String,
    'story_id': fields.Integer,
})

@api.route('/from_story/<int:key>', methods=["GET"])
class ChapterList(Resource):
    def get(self, key):
        return list_chapters(key)


@api.route('/<int:chapter_id>', methods=["GET"])
class ChapterDetail(Resource):
    def get(self, chapter_id):
        chapter = get_chapter(chapter_id)
        choices = list_chapter_choices(chapter_id)

        # Format objets_obtenus
        objets_obtenus = list_items_received(chapter_id)

        # Pour chaque choix, ajouter les objets requis
        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])

        # Ajouter les objets obtenus au chapitre
        chapter['objets_obtenus'] = objets_obtenus
        chapter['choices'] = choices

        return chapter