from flask import Flask
from .Models import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + "Application/Models/sqlite.db"
    )

    db.init_app(app)
    db.create_all()

    return app


app = create_app()

from .Views import routes