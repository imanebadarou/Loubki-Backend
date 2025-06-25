from flask_restx import Namespace, Resource, fields
from model.item import list_items, list_items_received, list_required_items

api = Namespace('Item', description='Gestion des objets')

objet = api.model('Item', {
    'id': fields.Integer,
    'label': fields.String,
})

@api.route('/')
class ItemList(Resource):
    def get(self):
        return list_items()

@api.route('/required_from_choice/<int:choice_id>/')
class ItemFromChoice(Resource):
    def get(self, choice_id):
        return list_required_items(choice_id)

@api.route('/received_from_chapter/<int:chapter_id>/')
class ItemFromChapter(Resource):
    def get(self, chapter_id):
        return list_items_received(chapter_id)