from app import db
import uuid
from datetime import datetime

class DetalleFactura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    cliente = db.Column(db.String(250))
    fecha = db.Column(db.Date)
    precio_total = db.Column(db.Float)

    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'))
    productos = db.relationship('Producto', backref='detalleFactura', lazy=True) # Uno a muchos