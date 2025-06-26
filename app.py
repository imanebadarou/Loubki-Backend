from flask import Flask
from flask_restx import Api
from db import close_connection

from api.story import api as story_ns
from api.choice import api as choice_ns
from api.chapter import api as chapter_ns
from api.item import api as item_ns
from api.receive import api as receive_ns
from api.required import api as required_ns

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Loubki API',
    description="Loubki est une application qui propose une narration dynamique où les choix des utilisateurs influencent le déroulement de l'histoire. Grâce à un système d'inventaire intégré, chaque utilisateur peut collecter, utiliser ou échanger des objets qui modifient les options narratives disponibles, enrichissant ainsi l'expérience de jeu. L'API offre des endpoints pour l’accès aux chapitres, la modification d'histoires et l'accès aux chapitres.")

api.add_namespace(story_ns,     path='/stories')
api.add_namespace(chapter_ns,   path='/chapters')
api.add_namespace(choice_ns,    path='/choices')
api.add_namespace(item_ns,      path='/items')
api.add_namespace(receive_ns,   path='/receive_links')
api.add_namespace(required_ns,  path='/required_links')

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def app_teardown(exception):
    """Close the database connection at the end of the request."""
    close_connection(exception)
