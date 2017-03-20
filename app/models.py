from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from app import login_manager
class Role(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(180))
    permissions = db.Column(db.Integer)
    users = db.relationship('User',backref = 'role',lazy = 'dynamic')
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nickname =db.Column(db.String(120),index = True,unique = True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index = True,unique = True)
    last_seen = db.Column(db.DateTime)
    posts = db.relationship('Post',backref = 'author',lazy = 'dynamic')
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)
    def __repr__(self):
        return '<User %r>' % (self.nickname)
class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String(160))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    def __reper__(self):
        return '<Post %r>' % (self.body)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
