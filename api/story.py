from flask_restx import Namespace, Resource, fields
from model.story import list_stories, get_story, create_story, update_story, delete_story

api = Namespace('Story', description='Gestion des histoires')

story = api.model('Story', {
    'id':           fields.Integer(readonly=True, description='Identifiant de l\'histoire'),
    'name':         fields.String(required=True, description='Nom de l\'histoire'),
    'img_url':      fields.String(required=True, description='URL de l\'image de l\'histoire'),
    'description':  fields.String(required=True, description='Description de l\'histoire'),
})

@api.route('/')
class StoryList(Resource):
    @api.marshal_list_with(story)
    def get(self):
        return list_stories()
    
    @api.expect(story)
    @api.marshal_with(story, code=201)
    def post(self):
        data = api.payload
        return create_story(data), 201

@api.route('/<int:id>')
class StoryDetail(Resource):
    @api.marshal_with(story)
    def get(self, id):
        return get_story(id)
    
    @api.expect(story)
    @api.marshal_with(story)
    def put(self, id):
        data = api.payload
        update_story(id, data)
        return get_story(id)

    @api.response(204, 'Story deleted')
    def delete(self, id):
        delete_story(id)