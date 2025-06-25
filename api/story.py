from flask_restx import Namespace, Resource, fields
from model.story import list_stories, get_story

api = Namespace('Story', description='Gestion des histoires')

histoire = api.model('Story', {
    'id': fields.Integer,
    'name': fields.String,
    'img_url': fields.Integer,
    'description': fields.Integer,
})

@api.route('/')
class Story(Resource):
    def get(self):
        return list_stories()


@api.route('/<int:key>', methods=["GET"])
class Story(Resource):
    def get(self, key):
        return get_story(key)