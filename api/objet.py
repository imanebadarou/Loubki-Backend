from flask_restx import Namespace, Resource, fields

api = Namespace('Objet', description='Gestion des objets')

objet = api.model('Objet', {
    'id_obj': fields.Integer,
    'nom_obj': fields.String,
})