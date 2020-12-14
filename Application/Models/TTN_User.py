from Application import db


class TTN_User(db.Model):
    __tablename__ = "TTN_User"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    broker = db.Column(db.String)
    topic = db.Column(db.String)

    def __repr__(self) -> str:
        return f"<TTN_User {self.user_id}>"