from .auth import User
import os
from flask import Flask, send_from_directory
from dotenv import load_dotenv
from flask_login import LoginManager

def create_app():
    load_dotenv()

    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    frontend_dir = os.path.join(template_dir, 'frontend')
    static_dir = os.path.join(frontend_dir, 'static')

    print(static_dir)

    app = Flask(__name__, static_url_path='', static_folder = static_dir, template_folder = frontend_dir)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')



    from .views import views
    from .request import request
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(request, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    # loginmanager for add data 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    
    # login User for add data 
    @login_manager.user_loader
    def load_user(id):
        return User(os.getenv('USER_PASSWORD'))


    return app

