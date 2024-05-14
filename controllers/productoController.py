from models.producto import Producto
from models.lote import Lote
from errors.errores import Errores
import uuid
from app import db
from datetime import datetime, timedelta, timezone
from flask import current_app
from models.estadoProducto import EstadoProducto

class ProductoController:

    # Metodo para listar productos
    def listar(self):
        return Producto.query.all()
    
    # Metodo para listar por external_id
    def listarPorExternalId(self, external_id):
        return Producto.query.filter_by(external_id=external_id).first()
    
    # Metodo para listar por estado
    def listarPorEstado(self, estado):
        return Producto.query.filter_by(estado=estado).all()
    
    # Metodo para registrar productos
    def registrar(self, data):
        try:
            # Verificar si ya existe un lote con el mismo nombre
            lote_existente = Lote.query.filter_by(nombre=data['nombre_lote']).first()
            if lote_existente:
                return Errores.error["-3"]

            # Crear lote
            lote = Lote(
                nombre=data['nombre_lote'],
                estado=True,
            )
            db.session.add(lote)
            db.session.commit()

            # Determinar el estado del producto basado en la fecha de caducidad
            fecha_caducidad = datetime.strptime(data['fecha_caducidad'], '%Y-%m-%d')
            if fecha_caducidad <= datetime.now():
                estado = EstadoProducto.CADUCADO
            elif fecha_caducidad <= datetime.now() + timedelta(days=5):
                estado = EstadoProducto.POR_CADUCAR
            else:
                estado = EstadoProducto.BUEN_ESTADO

            # Crear el producto
            producto = Producto(
                external_id = str(uuid.uuid4()),
                nombre = data['nombre'],
                fecha_caducidad = data['fecha_caducidad'],
                cantidad = data['cantidad'],
                precio_unitario = data['precio_unitario'],
                lote_id = lote.id,
                estado = estado
            )

            db.session.add(producto)
            db.session.commit()
            return producto
        except Exception as e:
            return Errores.error["-2"]