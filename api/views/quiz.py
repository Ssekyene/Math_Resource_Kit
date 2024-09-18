#!/usr/bin/python3
"""Routes for CRUD operations of the RESTful API for quizzes"""
from api.views import app_views
from models import storage
from models.concept import Concept
from flask import abort, request, jsonify

@app_views.route('/concepts/<concept_id>/quizzes', methods=['GET'], strict_slashes=False)
def get_quizzes(concept_id):
    """Returns quiz questions for a concept"""
    concept = storage.get(Concept, concept_id)
    if not concept:
        abort(404)
    quizzes = concept.quizzes
    quiz_data = []
    for quiz in quizzes:
        quiz_data.append(quiz.to_dict())
    return jsonify(quiz_data)


@app_views.route('/concepts/<concept_id>/quizzes', methods=['POST'], strict_slashes=False)
def get_score(concept_id):
    """Returns the number of correct quizzes and total quizzes"""
    concept = storage.get(Concept, concept_id)
    if not concept:
        abort(404)
    concept_quizzes = concept.quizzes
    total_quizzes = len(concept_quizzes)   
    data = request.get_json()
    if not data:
        abort(404, description="NOT A JSON")
    correct_quiz = 0
    for c_quiz in concept_quizzes:
        submitted_answer = data.get(c_quiz.id, "null")
        for option in c_quiz.options:
            if option.identifier == submitted_answer and option.identifier == c_quiz.correct_option:
                correct_quiz +=1
        print()
    return jsonify({"score": correct_quiz, "total": total_quizzes})
