from flask import Blueprint, jsonify, make_response, request

# Aqui importacion de los modelos de las tablas
from models.factura import Factura
from models.detalleFactura import DetalleFactura
from models.producto import Producto
from models.usuario import Usuario
from models.lote import Lote

api = Blueprint('api', __name__)
@api.route("/")
def home ():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )
