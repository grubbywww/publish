import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_pssword_setter(self):
        u = User(password = 'Cat')
        self.assertTrue(u.password_hash is not None)
    def test_password_verification(self):
        u = User(password = 'Cat')
        self.assertTrue(u.verify_password('Cat'))
        self.assertFalse(u.verify_password('Dog'))
        
