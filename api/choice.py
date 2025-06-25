from flask_restx import Namespace, Resource, fields
from model.choice import list_choices, get_choice, list_chapter_choices

api = Namespace('Choice', description='Gestion des choix d\'un chapitre')

choix = api.model('Choice', {
    'id': fields.Integer,
    'content': fields.String,
    'prev_chapter_id': fields.Integer,
    'next_chapter_id': fields.Integer,
})

@api.route('/')
class Choice(Resource):
    def get(self):
        return list_choices()
    
@api.route('/<key>', methods=["GET"])
class Choix(Resource):
    def get(self, key):
        return get_choice(key)
    
@api.route('/from_chapter/<int:chapter_id>', methods=["GET"])
class Choix(Resource):
    def get(self, chapter_id):
        return list_chapter_choices(chapter_id)