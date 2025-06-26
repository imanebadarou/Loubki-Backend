from flask_restx import Namespace, Resource, fields
from model.receive import create_receive, get_receive, update_receive, delete_receive
api = Namespace('Receive', description='Objets obtenus dans les chapitres')

receive = api.model('Receive', {
    'label': fields.String(readonly=True, description='Nom de l\'objet'),
    'quantity': fields.Integer(required=True, description='Quantité de l\'objet'),
    'chapter_id': fields.Integer(required=True, description='ID du chapitre d\'où l\'objet a été reçu'),
    'item_id': fields.Integer(required=True, description='ID de l\'objet reçu'),
})

@api.route('/')
class ReceiveList(Resource):
    @api.expect(receive)
    @api.marshal_with(receive, code=201)
    def post(self):
        data = api.payload
        chapter_id, item_id = create_receive(data)
        return get_receive(item_id, chapter_id), 201

@api.route('/<int:chapter_id>:<int:item_id>/')
class ReceiveDetail(Resource):
    @api.expect(receive)
    @api.marshal_with(receive)
    def put(self, chapter_id, item_id):
        data = api.payload
        update_receive(item_id, chapter_id, data)
        return get_receive(item_id, chapter_id)

    @api.response(204, 'Receive deleted')
    def delete(self, chapter_id, item_id):
        delete_receive(item_id, chapter_id)