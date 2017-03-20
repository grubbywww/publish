import os
from app import db
from app import create_app
from app.models import User,Post
from werkzeug.contrib.fixers import ProxyFix
app = create_app('default')
app.wsgi_app = ProxyFix(app.wsgi_app)
