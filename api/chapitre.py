from flask_restx import Namespace, Resource, fields
from model.chapitre import list_chap, chap_id
from model.choix import choix_chap
from model.objet import obj_obtenu_chap, obj_requis_choix

api = Namespace('Chapitre', description='Gestion des chapitres d\'une histoire')

chapitre = api.model('Chapitre', {
    'id_chap': fields.Integer,
    'nom_chap': fields.String,
    'contenu_chap': fields.String,
    'id_hist': fields.Integer,
})

@api.route('/<key>/chap', methods=["GET"])
class Chapitre(Resource):
    def get(self, key):
        chap_hist = list_chap(key)
        return chap_hist


@api.route('/<int:id_hist>/<int:id_chap>', methods=["GET"])
class ChapitreDetail(Resource):
    def get(self, id_hist, id_chap):
        chap_hist = chap_id(id_hist, id_chap)
        obj_obt = obj_obtenu_chap(id_chap)
        chap_chap = choix_chap(id_hist, id_chap)
        # on extrait les id_choix des choix du chapitre
        choix_ids = [choix['id_choix'] for choix in chap_chap]
        # on appelle obj_requis_choix pour chaque id_choix
        obj_req = [obj_requis_choix(id_choix) for id_choix in choix_ids]
        return {
            "chapitres": chap_hist,
            "objets_obtenus": obj_obt,
            "choix": chap_chap,
            "objets_requis": obj_req
        }