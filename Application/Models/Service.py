class Service(db.Model):
    __tablename__ = "Service"
    service_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String)
    status = db.Column(db.Integer)
    water_ml = db.Column(db.Integer)
    countdown_timer = db.Column(db.Integer)
    water_counter = db.Column(db.Integer)
    voltage_max = db.Column(db.Float)
    voltage_min = db.Column(db.Float)
    current_max = db.Column(db.Float)
    current_min = db.Column(db.Float)
    dev_id = db.Column(db.Integer, db.ForeignKey("Device.dev_id"))
    devices = db.relationship("Device", backref="device", uselist=False)

    def __repr__(self) -> str:
        return f"<Service {self.service_id}>"