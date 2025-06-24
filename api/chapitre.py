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

        # Format objets_obtenus
        objets_obtenus = [
            {
                "id": obj.get("id_obj"),
                "nom": obj.get("nom_obj"),
                "quantite": obj.get("quantite"),
            }
            for obj in obj_obt
        ]

        # Pour chaque choix, ajouter les objets requis
        choix_tab = []
        for choix in chap_chap:
            objets_requis = [
                {
                    "objet": obj_req.get("nom_obj"),
                    "perd_obj": obj_req.get("perd_obj"),
                }
                for obj_req in obj_requis_choix(choix["id_choix"])
            ]
            choix_tab.append({
                "id": choix.get("id_choix"),
                "text": choix.get("txt_choix"),
                "id_chap_next": choix.get("chap_next"),
                "objets_requis": objets_requis
            })

        chapitre = chap_hist[0] if isinstance(chap_hist, list) and chap_hist else chap_hist

        return {
            "id_chap": chapitre.get("id_chap"),
            "nom_chap": chapitre.get("nom_chap"),
            "contenu_chap": chapitre.get("contenu_chap"),
            "objets_obtenus": objets_obtenus,
            "choix": choix_tab
        }