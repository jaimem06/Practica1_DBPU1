from errors.errores import Errores
from models.usuario import Usuario
from models.usuario import Usuario
import uuid
from app import db
from datetime import datetime, timedelta, timezone
from flask import current_app
import jwt

class UsuarioController:

    def listar(self):
        return Usuario.query.all()
    
    def registrar(self, data):
        try:
            # Verificar si ya existe un usuario con el mismo correo
            usuario_existente = Usuario.query.filter_by(correo=data['correo']).first()
            if usuario_existente:
                return Errores.error["-3"]

            # Crear usuario
            usuario = Usuario(
                external_id = str(uuid.uuid4()),
                correo = data['correo'],
                clave = data['clave']
            )

            db.session.add(usuario)
            db.session.commit()

            return usuario
        except Exception as e:
            return Errores.error["-2"]
    
    # Metodo para iniciar sesión
    def login(self, data):
        usuarioA = Usuario.query.filter_by(correo = data.get('correo')).first()
        if usuarioA:
            # TODO encriptar
            if usuarioA.clave == data["clave"]:
                token = jwt.encode(
                    {
                        "external": usuarioA.external_id,
                        "expiracion": (datetime.now(timezone.utc) + timedelta(minutes=60)).isoformat()
                    }, 
                    key = current_app.config["SECRET_KEY"],
                    algorithm="HS512"
                )
                usuario = Usuario()
                usuario.copy(usuarioA)
                info = {
                    "token": token,
                    "user": usuarioA.correo
                }
                return info
            else:
                return -5
        else:
            return -5