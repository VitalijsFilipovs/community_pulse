from flask import Blueprint, request, jsonify
from app import db
from app.models.questions import Question
from app.schemas.question import QuestionCreate

router = Blueprint("questions", __name__, url_prefix="/questions")

@router.route("/", methods=["GET"])
def get_questions():
    questions = Question.query.all()
    return jsonify([
        {
            "id": q.id,
            "text": q.text,
            "category": {
                "id": q.category.id,
                "name": q.category.name
            } if q.category else None
        }
        for q in questions
    ])

@router.route("/", methods=["POST"])
def create_question():
    data = request.get_json()
    question_data = QuestionCreate(**data)
    question = Question(
        text=question_data.text,
        category_id=question_data.category_id  # добавляем использование category_id
    )
    db.session.add(question)
    db.session.commit()
    return jsonify({
        "id": question.id,
        "text": question.text,
        "category_id": question.category_id
    }), 201