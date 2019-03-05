from ws_api_tests_framework.src.handlers import BaseHandler


class SignupHandler(BaseHandler):
    def post(self, username, password, firstname, lastname):
        json = {
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname
        }

        response = self._post(
            url='/signup',
            json=json
        )

        return response





