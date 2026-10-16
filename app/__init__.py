import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Строка подключения собирается из переменных окружения
    db_user = os.environ.get("POSTGRES_USER", "app")
    db_password = os.environ.get("POSTGRES_PASSWORD", "changeme")
    db_host = os.environ.get("POSTGRES_HOST", "localhost")
    db_port = os.environ.get("POSTGRES_PORT", "5432")
    db_name = os.environ.get("POSTGRES_DB", "visits_db")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models import Visit  # noqa: F401
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()  

    return app