#!/usr/bin/python3
"""Routes for CRUD operations of the RESTful API for concepts"""
from api.views import app_views
from models import storage
from models.concept import Concept
from flask import jsonify, abort, request

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


@app_views.route('/concepts_search/<keyword>', methods=['GET'], strict_slashes=False)
def search_concepts(keyword):
    """Returns all concepts with a name matching the search keyword"""
    keyword = keyword.replace('_', ' ')
    matched_concepts = storage.concept_search(keyword)
    c_list = []
    for concept in matched_concepts:
        c_list.append(concept.to_dict())
    return jsonify(c_list)