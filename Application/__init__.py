from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists


app = Flask(__name__, template_folder="Templates")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "Models/sqlite.db"

db = SQLAlchemy(app)

from .Models import Connection, Device, Gateway, Service, TTN_User

if database_exists("sqlite:///" + "Models/sqlite.db"):
    db.init_app(app)
else:
    db.init_app(app)
    db.create_all()


from .Views import index, dashboard_view