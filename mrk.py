#!/usr/bin/python3
"""Starts a Flask web application for Maths Resource Kit.
"""
from flask import Flask, render_template, request, redirect, url_for
import uuid
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/mrk_hello")
def hello():
    """Return a hello message"""
    return "MRK Hello"


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


@app.route('/concept/<name>')
def concept(name):
    """returns a concept page"""
    # if not request.path.startswith('/concept/'):
    #     return redirect(url_for('/not_available/'))
    cache_id = (str(uuid.uuid4()))
    concept = storage.get_by_name("Concept", name)
    return render_template('concept.html', concept=concept, cache_id=cache_id)


@app.route('/about')
def about():
    """returns about page"""
    cache_id = (str(uuid.uuid4()))
    return render_template('about.html', cache_id=cache_id)


@app.teardown_appcontext
def teardown(exc):
    """
    release the current SQLAlchemy session after a transaction
    """
    storage.close()


host = '0.0.0.0'
port = 5000
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
