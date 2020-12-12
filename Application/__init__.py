from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "Models/sqlite.db"

    db = SQLAlchemy(app)

    if database_exists("sqlite:///" + "Models/sqlite.db"):
        db.init_app(app)
    else:
        db.init_app(app)
        db.create_all()

    return app


app = create_app()

from .Views import routes