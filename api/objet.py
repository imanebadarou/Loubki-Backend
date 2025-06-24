from flask_restx import Namespace, Resource, fields
from model.objet import list_obj, obj_requis, obj_requis_choix, obj_obtenus, obj_obtenu_chap

api = Namespace('Objet', description='Gestion des objets')

objet = api.model('Objet', {
    'id_obj': fields.Integer,
    'nom_obj': fields.String,
})

@api.route('/')
class Objet(Resource):
    def get(self):
        objets = list_obj()
        return objets

@api.route('/requis')
class Objet(Resource):
    def get(self):
        obj_req = obj_requis()
        return obj_req

@api.route('/<key>/requis')
class Objet(Resource):
    def get(self, key):
        obj_req_choix = obj_requis_choix(key)
        return obj_req_choix
    
@api.route('/obtenus')
class Objet(Resource):
    def get(self):
        obj_obtenu = obj_obtenus()
        return obj_obtenu
    
@api.route('/<key>/obtenus')
class Objet(Resource):
    def get(self, key):
        obj_obt_chap = obj_obtenu_chap(key)
        return obj_obt_chap