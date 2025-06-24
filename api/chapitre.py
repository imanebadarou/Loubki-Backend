from flask_restx import Namespace, Resource, fields

api = Namespace('Chapitre', description='Gestion des chapitres d\'une histoire')

chapitre = api.model('Chapitre', {
    'id_chap': fields.Integer,
    'nom_chap': fields.String,
    'contenu_chap': fields.String,
    'id_hist': fields.Integer,
})