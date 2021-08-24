from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session
import os, errno



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .request import request

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(request, url_prefix='/')

    from .models import schaetzen, two_idiots

    create_database(app)
    fill_database()

    return app


def create_database(app):
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    try:
        os.remove(db_path)
    except OSError as e: # this would be "except OSError
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred
    db.create_all(app=app)
    print('Created Database!')


def fill_database():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    engine = create_engine(db_uri)
    session = Session(engine)

    from website.models import schaetzen, two_idiots
    from faker import Faker
    faker = Faker()

    for i in range(1,100):
        spiel1 = schaetzen(frage = faker.text(max_nb_chars=80), antwort = faker.text(max_nb_chars=200), fun_fact = faker.text(max_nb_chars=80))
        spiel2 = two_idiots(categorie = faker.text(max_nb_chars=100))
        session.add(spiel1)
        session.add(spiel2)
    session.commit()

    print('Testdata were created')

    return