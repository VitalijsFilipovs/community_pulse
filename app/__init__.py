from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import questions, response  # Импорт моделей
    from app.routers import questions as questions_router
    from app.routers import response as response_router
    from app.routers import categories as categories_router   # ✅ импорт категорий

    # Регистрируем все роутеры:
    app.register_blueprint(questions_router.router)
    app.register_blueprint(response_router.router)
    app.register_blueprint(categories_router.router)           # ✅ регистрация категорий

    @app.route("/")
    def index():
        return "Добро пожаловать в Community Pulse!"

    return app