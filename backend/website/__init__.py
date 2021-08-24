from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    db.init_app(app)

    from .views import views
    from .request import request

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(request, url_prefix='/')

    from .models import schaetzen, two_idiots
    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
