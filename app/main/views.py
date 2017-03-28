from datetime import datetime
from flask import render_template,session,redirect,url_for,request,g,make_response
from flask.ext.login import logout_user,login_required
from . import main
from .. import db
from ..models import User,Post


@main.route('/',methods=['GET','POST'])
@login_required
def index():
    #u = User.query.filter_by(nickname = 'jonhson').first()
    #c = u.posts.all()
    #c = {'name':"susan"}
    name = request.cookies.get('cname')
    return render_template("index.html",name = name)
