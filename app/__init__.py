from flask import Flask,render_template
from flask.ext.mail import Mail
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import iconfig

mail = Mail()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(name):
    app = Flask(__name__)
    app.config.from_object(iconfig[name])
    iconfig[name].init_app(app)
    from .main import main as main_blue
    app.register_blueprint(main_blue)
    from .auth import auth as auth_blue
    app.register_blueprint(auth_blue,url_prefix='/auths')
    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    return app

