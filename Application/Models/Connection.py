from Application import db


class Connection(db.Model):
    __tablename__ = "Connection"
    conn_id = db.Column(db.Integer, primary_key=True)
    dev_id = db.Column(db.Integer, db.ForeignKey("Device.dev_id"))
    service_id = db.Column(db.Integer, db.ForeignKey("Service.service_id"))
    gateway_id = db.Column(db.Integer, db.ForeignKey("Gateway.gateway_id"))
    rssi = db.Column(db.Float)
    snr = db.Column(db.Float)

    devices = db.relationship("Device", foreign_keys=dev_id)
    services = db.relationship("Service", foreign_keys=service_id)
    gateways = db.relationship("Gateway", foreign_keys=gateway_id)

    def __repr__(self) -> str:
        return f"<Connection {self.conn_id}>"