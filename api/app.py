#!/usr/bin/python3
"""Flask Application for the RESTful API """
from flask import Flask, make_response, jsonify
from api.views import app_views
from flask_cors import CORS
from models import storage
from os import environ

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown(exc):
    """
    release the current SQLAlchemy session after a transaction
    """
    storage.close()

@app.errorhandler(404)
def not_found(err):
    """404 error"""
    return make_response(jsonify({"errror": "Not Found"}), 404)


if __name__ == '__main__':
    """Main function"""
    host = environ.get('host')
    port = environ.get('port')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5001
    app.run(host=host, port=port, threaded=True, debug=True)
