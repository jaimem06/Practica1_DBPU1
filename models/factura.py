from app import db
import uuid
from datetime import datetime

class Factura (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    detalle_fac = db.relationship('DetalleFactura', backref='factura', lazy=True) # Uno a muchos