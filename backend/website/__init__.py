import os
from flask import Flask
from dotenv import load_dotenv


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    # from .views import views
    from .request import request

    # app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(request, url_prefix='/')


    return app

