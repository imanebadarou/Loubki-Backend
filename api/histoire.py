from flask_restx import Namespace, Resource, fields
from model.histoire import list_histoires, histoire_id, histoire_choix

api = Namespace('Histoire', description='Gestion des histoires')

histoire = api.model('Histoire', {
    'id_hist': fields.Integer,
    'nom_hist': fields.String,
    'img_hist': fields.Integer,
    'resume_hist': fields.Integer,
})

@api.route('/')
class Histoire(Resource):
    def get(self):
        histoires = list_histoires()
        return histoires
    
@api.route('/<key>', methods=["GET"])
class Histoire(Resource):
    def get(self, key):
        histoireid = histoire_id(key)
        return histoireid

@api.route('/<key>/choix', methods=["GET"])
class Histoire(Resource):
    def get(self, key):
        histoireid = histoire_choix(key)
        return histoireid
