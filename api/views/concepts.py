#!/usr/bin/python3
"""Routes for CRUD operations of the RESTful API for concepts"""
from api.views import app_views
from models import storage
from models.concept import Concept
from flask import jsonify, abort

@app_views.route('/concepts', methods=['GET'], strict_slashes=False)
def get_concepts():
    """Returns all concept objects"""
    all_concepts = storage.all(Concept).values()
    concept_list =[]
    for concept in all_concepts:
        concept_list.append(concept.to_dict())
    return jsonify(concept_list)

@app_views.route('/concepts/<concept_id>', methods=['GET'], strict_slashes=False)
def get_concept(concept_id):
    """Returns a specific concept"""
    concept = storage.get(Concept, concept_id)
    if not concept:
        abort(404)
    return jsonify(concept.to_dict())
    
