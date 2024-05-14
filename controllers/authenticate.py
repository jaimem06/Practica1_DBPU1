from flask import request, jsonify, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
from errors.errores import Errores
import uuid
import jwt
from datetime import datetime, timedelta
from functools import wraps
from models.usuario import Usuario

def token_required(f):
    @wraps(f)
    # Es un componente para validar el token
    def decored(*args, **kwargs):
        token = None
        if 'X-Access-Tokens' in request.headers:
            token = request.headers['X-Access-Tokens']
        if not token:
            return make_response(
                jsonify({"msg": "ERROR", "code": 401, "datos":{"error":Errores.error["-4"]}}),
                401
            )
        try:
            data = jwt.decode(token, algorithms="HS512", key=current_app.config['SECRET_KEY'])
            user = Usuario.query.filter_by(external_id = data['external']).first()  # Use Usuario instead of Cuenta
            if not user:
                return make_response(
                    jsonify({"msg": "ERROR", "code": 401, "datos":{"error":Errores.error["-5"]}}),
                    401
                )
        except:
            return make_response(
                    jsonify({"msg": "ERROR", "code": 401, "datos":{"error":Errores.error["-5"]}}),
                    401
            )
        return f(*args, **kwargs)
    return decored