from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


from .Users import TTN_User
from .Device import Device
from .Service import Service
from .Gateway import Gateway
from .Connection import Connection
