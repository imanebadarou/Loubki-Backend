from flask_restx import Namespace, Resource, fields
from model.story import list_stories, get_story, create_story, update_story, delete_story
from model.chapter import create_chapter

api = Namespace('Story', description='Gestion des histoires')

story = api.model('Story', {
    'id':           fields.Integer(readonly=True, description='Identifiant de l\'histoire'),
    'name':         fields.String(required=True, description='Nom de l\'histoire'),
    'img_url':      fields.String(required=True, description='URL de l\'image de l\'histoire'),
    'description':  fields.String(required=True, description='Description de l\'histoire'),
    'first_chapter_id':  fields.Integer(required=True, description='Identifiant du premier chapitre de l\'histoire'),
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
        id = create_story(data)
        chapter_id = create_chapter({
            'name': 'Sans titre',
            'content': '',
            'story_id': id,
            'prev_choice_id': None
        })
        update_story(id, {'first_chapter_id': chapter_id})
        return get_story(id), 201

@api.route('/<int:id>')
class StoryDetail(Resource):
    @api.marshal_with(story)
    def get(self, id):
        story = get_story(id)
        if not story:
            api.abort(404, f"Story with id {id} not found")
        return story

    @api.expect(story)
    @api.marshal_with(story)
    def put(self, id):
        data = api.payload
        if update_story(id, data):
            return get_story(id)
        else:
            api.abort(404, f"Story with id {id} not found")

    @api.response(204, 'Story deleted')
    def delete(self, id):
        if not delete_story(id):
            api.abort(404, f"Story with id {id} not found")