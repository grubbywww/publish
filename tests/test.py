#! venv/bin/python
import unittest
from app import create_app,db
from app.models import User,Post
from flask import current_app
import datetime
class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('default')
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.create_all()
    def tearDown(self):
        #db.session.remove()
        #db.drop_all()
        self.app_context.pop()
    def test_testing(self):
        self.assertTrue(current_app.config['TESTING'])
    def test_user_post(self):
        u = User(nickname = 'susan',email = 'susan@email.com',last_seen = datetime.datetime.utcnow())
        u.password='123'
        db.session.add(u)
        db.session.commit()
        users = User.query.filter_by(nickname = 'susan').first()
        p = Post(body = 'First article',timestamp = datetime.datetime.utcnow(),author = users)
        db.session.add(p)
        db.session.commit()
        email = ""
        r = User.query.filter_by(nickname = 'susan').first()
        c = r.posts.all()
        for i in c:
            email = i.author.email
        assert email == 'susan@email.com'
