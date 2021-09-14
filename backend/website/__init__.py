import os
from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager

def create_app():
    load_dotenv()

    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'frontend')

    app = Flask(__name__, template_folder = template_dir)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    from .views import views
    from .request import request
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(request, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return True


    return app

