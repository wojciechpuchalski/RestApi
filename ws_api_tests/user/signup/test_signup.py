import unittest


from ws_api_tests_framework.src.handlers.signup import SignupHandler
from ws_api_tests_framework.src.actors import Actor


class SignupTestSuite(unittest.TestCase):
    def setUp(self):
        self.actor = Actor()

    def test_signup(self):
        r = SignupHandler(actor=self.actor).post(
            username=self.actor.username,
            password=self.actor.password,
            firstname=self.actor.firstname,
            lastname=self.actor.lastname,
        )

        user_model = r.json()

        # Assert
        self.assertIn("createdAt", user_model)
        self.assertIn("updatedAt", user_model)
        self.assertIn("id", user_model)
        self.assertIn("modelType", user_model)
        self.assertIn("username", user_model)
        self.assertIn("firstname", user_model)
        self.assertIn("lastname", user_model)

        # Assert correct values in return
        self.assertEqual("UserModel", user_model["modelType"])
        self.assertEqual(self.actor.username, user_model["username"])
        self.assertEqual(self.actor.firstname, user_model["firstname"])
        self.assertEqual(self.actor.lastname, user_model["lastname"])