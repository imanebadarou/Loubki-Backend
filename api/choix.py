from flask_restx import Namespace, Resource, fields
from model.choix import list_choix, choix_id

api = Namespace('Choix', description='Gestion des choix d\'un chapitre')

choix = api.model('Choix', {
    'id_choix': fields.Integer,
    'txt_choix': fields.String,
    'chap_prev': fields.Integer,
    'chap_next': fields.Integer,
})

@api.route('/')
class Choix(Resource):
    def get(self):
        choix = list_choix()
        return choix
    
@api.route('/<key>', methods=["GET"])
class Choix(Resource):
    def get(self, key):
        choixid = choix_id(key)
        return choixid