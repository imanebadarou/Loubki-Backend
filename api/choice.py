from flask_restx import Namespace, Resource, fields
from model.choice import list_choices, get_choice, list_chapter_choices
from model.item import list_required_items

api = Namespace('Choice', description='Gestion des choix d\'un chapitre')

choice = api.model('Choice', {
    'id': fields.Integer,
    'content': fields.String,
    'prev_chapter_id': fields.Integer,
    'next_chapter_id': fields.Integer,
})

@api.route('/from_story/<int:story_id>', methods=["GET"])
class ChoiceFromStory(Resource):
    def get(self, story_id):
        choices = list_choices(story_id)

        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])
            
        return choices
    
@api.route('/<int:key>', methods=["GET"])
class ChoiceDetail(Resource):
    def get(self, key):
        return get_choice(key)
    
@api.route('/from_chapter/<int:chapter_id>', methods=["GET"])
class ChoiceFromChapter(Resource):
    def get(self, chapter_id):
        return list_chapter_choices(chapter_id)