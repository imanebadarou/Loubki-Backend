from flask import Flask, render_template
from model import close_connection, list_histoires
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