from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from app import login_manager

class Permission:
    CREATE_TASK = 0x01
    VERIFY_TASK = 0x02
    RELEASE_TASK = 0x04
    CHECK_TASK = 0X08
    #CREATE_OPERATOR = 0X10
    #CHECK_RESOURCE = 0x20
    #APPLICATION_RESOURCE = 0X40
    #CREATE_APPLICATION = 0x80

class Role(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(180))
    permissions = db.Column(db.Integer)
    users = db.relationship('User',backref = 'role',lazy = 'dynamic')
    @staticmethod
    def insert_roles():
        roles = {
            'EXECUTOR':(Permission.CREATE_TASK | Permission.VERIFY_TASK | Permission.RELEASE_TASK)
        }
        for r in roles:
            role = Role.query.filter_by(name = r).first()
            if role is None:
                role = Role(name = r)
            role.permissions = roles[r][0]
            db.session.add(role)
        db.session.commit()

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
