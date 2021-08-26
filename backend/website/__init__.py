from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///data/{DB_NAME}'
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

    try:
        if os.path.exists('website/data/' + DB_NAME):
            print('Old Database will be deleted')
            os.remove('website/data/' + f'{DB_NAME}')

    except FileNotFoundError:
        print('Cannot find old Database')

    db.create_all(app=app)
    print('Created a new Database!')

