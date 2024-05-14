from flask import Blueprint, jsonify, make_response, request
from controllers.usuarioController import UsuarioController
from models.usuario import Usuario
from controllers.authenticate import token_required

api_usuario = Blueprint('api_usuario', __name__)

usuarioC = UsuarioController()

# API para listar usuario
@api_usuario.route("/usuario")
@token_required
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [i.serialize for i in usuarioC.listar()]}),
        200
    )

# API para iniciar sesión
@api_usuario.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    result = usuarioC.login(data)
    if isinstance(result, dict):
        return jsonify(result), 200
    else:
        return jsonify({"error": "Correo o clave incorrectos"}), 401

# API para registrar usuario
@api_usuario.route("/usuario/registrar", methods=['POST'])
@token_required
def registrar():
    data = request.get_json()
    result = usuarioC.registrar(data)
    if isinstance(result, Usuario):
        return jsonify({"msg": "Usuario registrado con éxito"}), 201
    else:
        return jsonify({"error": "Error al registrar usuario"}), 500