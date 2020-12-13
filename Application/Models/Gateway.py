class Gateway(db.Model):
    __tablename__ = "Gateway"
    gateway_id = db.Column(db.Integer, primary_key=True)
    gtw_id = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    location = db.Column(db.String)

    def __repr__(self) -> str:
        return f"<Gateway {self.gateway_id}>"