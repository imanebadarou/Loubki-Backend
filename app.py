from flask import Flask, render_template
from model import *
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def app_teardown(exception):
    """Close the database connection at the end of the request."""
    close_connection(exception)

@api.route('/histoires')
class Histoire(Resource):
    def get(self):
        histoires = list_histoires()
        return histoires
    
@api.route('/histoire/<key>', methods=["GET"])
class Histoire(Resource):
    def get(self, key):
        histoireid = histoire_id(key)
        return histoireid

@api.route('/histoire/<key>/choix', methods=["GET"])
class Histoire(Resource):
    def get(self, key):
        histoireid = histoire_choix(key)
        return histoireid

@api.route('/choix')
class Choix(Resource):
    def get(self):
        choix = list_choix()
        return choix
    
@api.route('/choix/<key>', methods=["GET"])
class Choix(Resource):
    def get(self, key):
        choixid = choix_id(key)
        return choixid