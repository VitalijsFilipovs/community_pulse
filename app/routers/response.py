from flask import Blueprint, request, jsonify
from app import db
from app.models.response import Response
from app.models.questions import Question
from app.schemas.response import ResponseCreate, ResponseStats

router = Blueprint("responses", __name__, url_prefix="/responses")


@router.route("/", methods=["POST"])
def create_response():
    data = request.get_json()
    response_data = ResponseCreate(**data)

    # Создаём и сохраняем новый ответ
    response = Response(
        question_id=response_data.question_id,
        is_agree=response_data.is_agree
    )
    db.session.add(response)
    db.session.commit()

    return jsonify({
        "id": response.id,  # можно сразу возвращать ID созданного ответа
        "question_id": response.question_id,
        "is_agree": response.is_agree
    }), 201


@router.route("/", methods=["GET"])
def get_stats():
    questions = Question.query.all()
    stats = []
    for question in questions:
        agree_count = Response.query.filter_by(question_id=question.id, is_agree=True).count()
        disagree_count = Response.query.filter_by(question_id=question.id, is_agree=False).count()
        stats.append({
            "question_id": question.id,
            "agree_count": agree_count,
            "disagree_count": disagree_count
        })
    return jsonify(stats)

@router.route("/all", methods=["GET"])
def get_all_responses():
    responses = Response.query.all()
    return jsonify([
        {
            "id": r.id,
            "question_id": r.question_id,
            "is_agree": r.is_agree
        }
        for r in responses
    ])