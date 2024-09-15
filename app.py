"""Starts a Flask web application.
"""
from flask import Flask, render_template
import uuid
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
@app.route("/home/")
def home():
    """Returns home page"""
    cache_id = (str(uuid.uuid4()))
    return render_template("index.html", cache_id=cache_id)


@app.route('/not_available/')
def not_available():
    """returns not available page"""
    cache_id = (str(uuid.uuid4()))
    return render_template("not_available.html", cache_id=cache_id)


@app.route('/concept_list/')
def concept_list():
    """Returns a concept list page"""
    cache_id = (str(uuid.uuid4()))
    concepts = storage.all("Concept")
    return render_template('concept_list.html', concepts=concepts, cache_id=cache_id)


@app.route('/concept/')
def concept():
    """returns a concept page"""
    cache_id = (str(uuid.uuid4()))
    return render_template('concept.html', cache_id=cache_id)


host = '0.0.0.0'
port = 5000
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)