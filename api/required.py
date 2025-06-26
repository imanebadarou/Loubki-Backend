from flask_restx import Namespace, Resource, fields
from model.required import create_required, get_required, update_required, delete_required
api = Namespace('Required', description='Objets obtenus dans les chapitres')

required = api.model('Required', {
    'label': fields.String(readonly=True, description='Nom de l\'objet'),
    'quantity': fields.Integer(required=True, description='Quantité de l\'objet'),
    'choice_id': fields.Integer(required=True, description='ID du chapitre d\'où l\'objet a été reçu'),
    'item_id': fields.Integer(required=True, description='ID de l\'objet reçu'),
    'lose_item': fields.Boolean(required=True, description='Indique si l\'objet est perdu après utilisation'),
})

@api.route('/')
class RequiredList(Resource):
    @api.expect(required)
    @api.marshal_with(required, code=201)
    def post(self):
        data = api.payload
        choice_id, item_id = create_required(data)
        return get_required(item_id, choice_id), 201

@api.route('/<int:choice_id>:<int:item_id>/')
class RequiredDetail(Resource):
    @api.expect(required)
    @api.marshal_with(required)
    def put(self, choice_id, item_id):
        data = api.payload
        update_required(item_id, choice_id, data)
        return get_required(item_id, choice_id)

    @api.response(204, 'Required deleted')
    def delete(self, choice_id, item_id):
        delete_required(item_id, choice_id)