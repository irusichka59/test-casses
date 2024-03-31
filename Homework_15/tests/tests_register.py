from Homework_15.api import BaseApi

from Homework_15.tests.constants import register_url


class TestRegister:
    base_api = BaseApi()

    def test_register_successful(self):
        response = self.base_api.post(register_url, body={"email": "eve.holt@reqres.in", "password": "pistol"})
        assert response.status_code == 200
        assert 'id' in response.json()
        assert 'token' in response.json()
        assert response.json()['id'] != ''
        assert response.json()['token'] != ''

    def test_register_unsuccessful(self):
        response = self.base_api.post(register_url, body={"email": "sydney@fife"})
        assert response.status_code == 400
        assert 'error' in response.json()
