import flask

from .bar.views import hello

app = flask.Flask(__name__)


@app.route('/')
def home():
    return hello()

