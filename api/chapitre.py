from flask_restx import Namespace, Resource, fields
from model.chapitre import list_chap

api = Namespace('Chapitre', description='Gestion des chapitres d\'une histoire')

chapitre = api.model('Chapitre', {
    'id_chap': fields.Integer,
    'nom_chap': fields.String,
    'contenu_chap': fields.String,
    'id_hist': fields.Integer,
})

@api.route('/<key>/chap', methods=["GET"])
class Chapitre(Resource):
    def get(self, key):
        chapid = list_chap(key)
        return chapid