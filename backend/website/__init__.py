import os
from flask import Flask
from dotenv import load_dotenv


def create_app():
    load_dotenv()

    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'frontend')

    app = Flask(__name__, template_folder = template_dir)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    from .views import views
    from .request import request

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(request, url_prefix='/')


    return app

