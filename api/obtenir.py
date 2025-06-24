from flask_restx import Namespace, Resource, fields

api = Namespace('Obtenir', description='Objets obtenus dans les chapitres')

obtenir = api.model('Obtenir', {
    'id_obj': fields.Integer,
    'id_chap': fields.Integer,
    'quantite': fields.Integer,
})