import unittest
from uuid import uuid4
import requests
import pprint


class SignupTestSuite(unittest.TestCase):

    def test_signup(self):
        username = uuid4().hex[:20]
        url = 'http://18.195.167.117:5000/signup'
        r=requests.post(
            url, json={
                "username": "Wojciech456",
                "password": "testowehaslo1",
                "firstname": username,
                "lastname": "TestoweNazwisko"

                }
        )
        user_model = r.json()

        # Assert model structure
        self.assertIn("createdAt", user_model)
        self.assertIn("updatedAt", user_model)
        self.assertIn("id", user_model)
        self.assertIn("modelType", user_model)
        self.assertIn("username", user_model)
        self.assertIn("firstname", user_model)
        self.assertIn("lastname", user_model)

        # Assert correct values in return
        self.assertEqual("UserModel", user_model["modelType"])
        self.assertEqual(username, user_model["username"])
        self.assertEqual("test1", user_model["firstname"])
        self.assertEqual("test2", user_model["lastname"])
