from flask_restx import Namespace, Resource, fields
from model.choice import list_choices, get_choice, list_chapter_choices
from model.item import list_required_items
from api.item import item

api = Namespace('Choice', description='Gestion des choix d\'un chapitre')

choice = api.model('Choice', {
    'id': fields.Integer,
    'content': fields.String,
    'prev_chapter_id': fields.Integer,
    'next_chapter_id': fields.Integer,
    'required_items': fields.List(fields.Nested(item)),  # Utilisation de Raw pour les items requis
})

@api.route('/from_story/<int:story_id>', methods=["GET"])
class ChoiceFromStory(Resource):
    @api.marshal_list_with(choice)
    def get(self, story_id):
        choices = list_choices(story_id)

        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])
            
        return choices
    
@api.route('/<int:id>', methods=["GET"])
class ChoiceDetail(Resource):
    @api.marshal_with(choice)
    def get(self, id):
        choice = get_choice(id)
        choice['required_items'] = list_required_items(id)
        return choice
    
@api.route('/from_chapter/<int:chapter_id>', methods=["GET"])
class ChoiceFromChapter(Resource):
    @api.marshal_list_with(choice)
    def get(self, chapter_id):
        choices = list_chapter_choices(chapter_id)

        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])
        return choices