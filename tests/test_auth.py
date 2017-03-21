import unittest
from app import create_app,db
from app.models import User,Role,Permission

#class UserModelTestCase(unittest.TestCase):
    #def test_pssword_setter(self):
    #    u = User(password = 'Cat')
    #    self.assertTrue(u.password_hash is not None)
    #def test_password_verification(self):
    #    u = User(password = 'Cat')
    #    self.assertTrue(u.verify_password('Cat'))
    #    self.assertFalse(u.verify_password('Dog'))

class UserRoleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('default')
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.create_all()
    def tearDown(self):
        #db.session.remove()
        #db.drop_all()
        self.app_context.pop()
    def test_role(self):
        u = User(nickname = 'susan').query.first()
        u.role_id = 2
        db.session.add(u)
        db.session.commit()
        self.assertTrue(u.can(Permission.CREATE_TASK))

