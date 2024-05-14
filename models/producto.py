from app import db
import uuid
from datetime import datetime, timedelta
from models.estadoProducto import EstadoProducto
from models.lote import Lote
from models.detalleFactura import DetalleFactura

class Producto (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    nombre = db.Column(db.String(250))
    fecha_caducidad = db.Column(db.Date)
    cantidad = db.Column(db.Integer)
    precio_unitario = db.Column(db.Float)
    stock = db.Column(db.Boolean, default=True)
    estado = db.Column(db.Enum(EstadoProducto))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    detalle_fact_id = db.Column(db.Integer, db.ForeignKey(DetalleFactura.id))
    lote_id = db.Column(db.Integer, db.ForeignKey(Lote.id))

    @property
    def serialize(self):
        return {
            'external_id': self.external_id,
            'nombre': self.nombre,
            'fecha_caducidad': self.fecha_caducidad,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'stock': self.stock,
            'estado': self.estado.name if self.estado else None,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'detalle_fact_id': self.detalle_fact_id,
            'lote_id': self.lote_id
        }
    
    def copy(self):
        return Producto(
            nombre = self.nombre,
            fecha_caducidad = self.fecha_caducidad,
            cantidad = self.cantidad,
            precio_unitario = self.precio_unitario,
            stock = self.stock,
            estado = self.estado,
            detalle_fact_id = self.detalle_fact_id,
            lote_id = self.lote_id
        )
    
    ## Actualizar el estado del producto en la base de datos
    def actualizar_estado(self):
        fecha_caducidad = datetime.strptime(self.fecha_caducidad, '%Y-%m-%d')
        if fecha_caducidad <= datetime.now():
            self.estado = EstadoProducto.CADUCADO
            self.stock = False  # Cambiar el stock a falso
        elif fecha_caducidad <= datetime.now() + timedelta(days=5):
            self.estado = EstadoProducto.POR_CADUCAR
        else:
            self.estado = EstadoProducto.BUEN_ESTADO
        db.session.commit()