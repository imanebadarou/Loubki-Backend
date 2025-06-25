from flask import Flask
from flask_restx import Api
from db import close_connection

from api.story import api as story_ns
from api.choice import api as choice_ns
from api.chapter import api as chapter_ns
from api.item import api as item_ns

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app, version='Beta', title='Loubki API',
    description='API de l\'application Loubki')

api.add_namespace(story_ns,     path='/stories')
api.add_namespace(choice_ns,    path='/choices')
api.add_namespace(chapter_ns,   path='/chapters')
api.add_namespace(item_ns,      path='/items')

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def app_teardown(exception):
    """Close the database connection at the end of the request."""
    close_connection(exception)
