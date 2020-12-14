from Application import db


class Connection(db.Model):
    __tablename__ = "Connection"
    conn_id = db.Column(db.Integer, primary_key=True)
    dev_id = db.Column(db.Integer, db.ForeignKey("Device.dev_id"))
    service_id = db.Column(db.Integer, db.ForeignKey("Service.service_id"))
    gateway_id = db.Column(db.Integer, db.ForeignKey("Gateway.gateway_id"))
    rssi = db.Column(db.Float)
    snr = db.Column(db.Float)

    devices = db.relationship("Device", backref="device", uselist=False)
    services = db.relationship("Service", backref="service", uselist=False)
    gateways = db.relationship("Gateway", backref="gateway", uselist=False)

    def __repr__(self) -> str:
        return f"<Connection {self.conn_id}>"