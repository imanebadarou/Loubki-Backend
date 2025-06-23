from flask import Flask, render_template
from model import close_connection, list_histoires

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    histoires = list_histoires()
    return render_template('home.html', histoires=histoires)

@app.teardown_appcontext
def app_teardown(exception):
    """Close the database connection at the end of the request."""
    close_connection(exception)