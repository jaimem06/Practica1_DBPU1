from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    #TODO
    app.config.from_object('config.config.Config')
    db.init_app(app)

    with app.app_context():
        from routes.api import api
        from routes.apiProducto import api_producto
        from routes.apiUsuario import api_usuario
        app.register_blueprint(api)
        app.register_blueprint(api_producto)
        app.register_blueprint(api_usuario)
        # Creacion de las tablas
        db.create_all()
        #db.drop_all()
    return app