import requests

from Homework_15.tests.constants import login_successful


class TestLogin:
    def setup_method(self):
        self.session = requests.Session()

    def teardown_method(self):
        self.session.close()

    def test_post_login_successful(self):
        response = self.session.post(url=login_successful, data=
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        assert response.status_code == 200
        assert 'token' in response.json()
        assert response.json()['token'] != ''

    def test_post_login_unsuccessful(self):
        response = self.session.post(url=login_successful, data=
        {
            "email": "peter@klaven"
        })
        assert response.status_code == 400
        assert 'error' in response.json()
        assert response.json()['error'] != ''

