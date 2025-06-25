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

api.add_namespace(story_ns,     path='/story')
api.add_namespace(choice_ns,    path='/choice')
api.add_namespace(chapter_ns,   path='/chapter')
api.add_namespace(item_ns,      path='/item')

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def app_teardown(exception):
    """Close the database connection at the end of the request."""
    close_connection(exception)
