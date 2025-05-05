import unittest
from app.models.user import User

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.user = User(username="testuser", password="testpassword")

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpassword"))

    def test_user_str(self):
        self.assertEqual(str(self.user), "testuser")

    def test_user_password_hashing(self):
        self.assertNotEqual(self.user.password, "testpassword")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertFalse(self.user.check_password("wrongpassword"))

if __name__ == '__main__':
    unittest.main()