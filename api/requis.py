from flask_restx import Namespace, Resource, fields

api = Namespace('Requis', description='Objets requis pour faire certains choix')

requis = api.model('Requis', {
    'id_obj': fields.Integer,
    'id_choix': fields.Integer,
    'perd_obj': fields.Boolean,
})