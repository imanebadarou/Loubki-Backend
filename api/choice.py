from flask_restx import Namespace, Resource, fields
from model.choice import list_choices, get_choice, list_chapter_choices, create_choice, update_choice, delete_choice
from model.item import list_required_items
from model.chapter import create_chapter, get_chapter, delete_chapter
from api.item import item

api = Namespace('Choice', description='Gestion des choix d\'un chapitre')

choice = api.model('Choice', {
    'id': fields.Integer(readonly=True, description='ID du choix'),
    'content': fields.String(required=True, description="Description de l'action"),
    'prev_chapter_id': fields.Integer(required=True, description="ID du chapitre auquel ce choix est rattaché"),
    'next_chapter_id': fields.Integer(readonly=True, description="ID du chapitre vers lequel ce choix renvoie"),
    'required_items': fields.List(fields.Nested(item), readonly=True),
})

@api.route('/')
class ChoiceList(Resource):
    @api.expect(choice)
    @api.marshal_with(choice, code=201)
    def post(self):
        data = api.payload
        id = create_choice(data)
        new_choice = get_choice(id)
        new_choice['required_items'] = list_required_items(id)
        prev_chapter = get_chapter(new_choice['prev_chapter_id'])
        create_chapter({
            'name': 'Sans titre',
            'content': '',
            'story_id': prev_chapter['story_id'],
            'prev_choice_id': id
        })
        return new_choice, 201

@api.route('/<int:id>')
class ChoiceDetail(Resource):
    @api.marshal_with(choice)
    def get(self, id):
        choice = get_choice(id)
        choice['required_items'] = list_required_items(id)
        return choice
    
    @api.expect(choice)
    @api.marshal_with(choice)
    def put(self, id):
        data = api.payload
        update_choice(id, data)
        updated_choice = get_choice(id)
        updated_choice['required_items'] = list_required_items(id)
        return updated_choice

    @api.response(204, 'Choice deleted')
    def delete(self, id):
        choice = get_choice(id)
        delete_choice(id)
        delete_chapter(choice['next_chapter_id'])

@api.route('/from_story/<int:story_id>', methods=["GET"])
class ChoiceFromStory(Resource):
    @api.marshal_list_with(choice)
    def get(self, story_id):
        choices = list_choices(story_id)

        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])
            
        return choices
    
@api.route('/from_chapter/<int:chapter_id>', methods=["GET"])
class ChoiceFromChapter(Resource):
    @api.marshal_list_with(choice)
    def get(self, chapter_id):
        choices = list_chapter_choices(chapter_id)

        for choice in choices:
            choice['required_items'] = list_required_items(choice['id'])
        return choices