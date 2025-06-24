from flask import Flask
from flask_restx import Api
from db import close_connection

from api.histoire import api as histoire_ns
from api.choix import api as choix_ns
from api.chapitre import api as chapitre_ns
from api.objet import api as objet_ns
from api.obtenir import api as obtenir_ns
from api.requis import api as requis_ns

app = Flask(__name__)
api = Api(app, version='Beta', title='Loubki API',
    description='API de l\'application Loubki')

api.add_namespace(histoire_ns,  path='/histoire')
api.add_namespace(choix_ns,     path='/choix')
api.add_namespace(chapitre_ns,  path='/chapitre')
api.add_namespace(objet_ns,     path='/objet')
api.add_namespace(obtenir_ns,   path='/obtenir')
api.add_namespace(requis_ns,    path='/requis')

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def app_teardown(exception):
    """Close the database connection at the end of the request."""
    close_connection(exception)