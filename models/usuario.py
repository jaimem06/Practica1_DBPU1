from app import db
import uuid
from datetime import datetime

class Usuario (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    correo = db.Column(db.String(250))
    clave = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    facturas = db.relationship('Factura', backref='usuario')

    @property
    def serialize(self):
        return {
            'external_id': self.external_id,
            'correo': self.correo,
            'clave': self.clave,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def copy(self, other):
        self.external_id = other.external_id
        self.correo = other.correo
        self.clave = other.clave
        self.created_at = other.created_at
        self.updated_at = other.updated_at