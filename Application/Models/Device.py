from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Device(db.Model):
    __tablename__ = "Device"
    dev_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    location = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("TTN_User.user_id"))
    users = db.relationship("TTN_User", backref="user", uselist=False)

    def __repr__(self) -> str:
        return f"<Device {self.dev_id}>"