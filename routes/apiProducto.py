from flask import Blueprint, jsonify, make_response, request
from controllers.productoController import ProductoController
from models.producto import Producto
from errors.errores import Errores
from flask_expects_json import expects_json
from schemas.schemasProducto import schemaProducto
from controllers.authenticate import token_required

api_producto = Blueprint('api_producto', __name__)

productoC = ProductoController()

# API para listar producto
@api_producto.route("/producto")
@token_required
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [i.serialize for i in productoC.listar()]}),
        200
    )

# API listar por external_id
@api_producto.route("/producto/<external_id>")
@token_required
def listarPorExternalId(external_id):
    producto = Producto.query.filter_by(external_id=external_id).first()
    if producto:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": producto.serialize}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": Errores.error["-1"], "code": 400}),
            400
        )

# API para listar por estado
@api_producto.route("/producto/estado/<estado>")
@token_required
def listarPorEstado(estado):
    productos = Producto.query.filter_by(estado=estado).all()
    if productos:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": [i.serialize for i in productos]}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": Errores.error["-1"], "code": 400}),
            400
        )

# API para registrar producto
@api_producto.route("/producto/registrar", methods=["POST"])
@token_required
@expects_json(schemaProducto)
def registrar():
    data = request.json
    response = productoC.registrar(data)
    if isinstance(response, Producto):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": response.serialize}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": response, "code": 400}),
            400
        )