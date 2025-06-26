from flask_restx import Namespace, Resource, fields
from model.item import list_items, get_item, list_items_received, list_required_items, create_item, update_item, delete_item

api = Namespace('Item', description='Gestion des objets')

item = api.model('Item', {
    'id': fields.Integer(readonly=True, description='Identifiant de l\'objet'),
    'label': fields.String(required=True, description='Nom de l\'objet'),
})

@api.route('/')
class ItemList(Resource):
    @api.marshal_list_with(item)
    def get(self):
        return list_items()

    @api.expect(item)
    @api.marshal_with(item, code=201)
    def post(self):
        data = api.payload
        id = create_item(data)
        return get_item(id), 201


@api.route('/<int:id>/')
class ItemResource(Resource):
    @api.marshal_with(item)
    def get(self, id):
        item = get_item(id)
        if not item:
            api.abort(404, f"Item with id {id} not found")
        return item

    @api.expect(item)
    @api.marshal_with(item)
    def put(self, id):
        data = api.payload
        if update_item(id, data):
            return get_item(id)
        else:
            api.abort(404, f"Item with id {id} not found")

    @api.response(204, 'Item deleted')
    def delete(self, id):
        if not delete_item(id):
            api.abort(404, f"Item with id {id} not found")


@api.route('/required_from_choice/<int:choice_id>/')
class ItemFromChoice(Resource):
    @api.marshal_list_with(item)
    def get(self, choice_id):
        return list_required_items(choice_id)


@api.route('/received_from_chapter/<int:chapter_id>/')
class ItemFromChapter(Resource):
    def get(self, chapter_id):
        return list_items_received(chapter_id)