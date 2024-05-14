from app import db
from datetime import datetime

class Lote (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    productos = db.relationship('Producto', backref='lote', lazy=True) #Relación de uno a muchos