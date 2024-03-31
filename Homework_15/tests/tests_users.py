from Homework_15.api import BaseApi
from Homework_15.tests.constants import users_url, list_users, update_url, delayed_url, not_found


class TestUsers:
    def setup_method(self):
        self.base_api = BaseApi()

    def teardown_method(self):
        del self.base_api

    def test_get_all_users_are_unique(self):
        response = self.base_api.get(url=users_url)
        assert response.status_code == 200
        ids = [k['id'] for k in response.json()['data']]
        assert len(set(ids)) == len(ids)

    def test_get_list_users(self):
        response = self.base_api.get(url=list_users)
        assert response.status_code == 200
        ids = [k['id'] for k in response.json()['data']]
        assert len(set(ids)) == len(ids)

    def test_post_create_user(self):
        response = self.base_api.post(url=users_url, body=
        {
            "name": "morpheus",
            "job": "leader"
        })
        assert response.status_code == 201
        assert response.json().get('id')

    def test_put_update_user(self):
        response = self.base_api.put(url=update_url, body=
        {
            "name": "morpheus",
            "job": "zion resident"
        })
        assert response.status_code == 200
        # Перевіряємо, що дані про користувача були оновлені
        assert response.json().get('name') == 'morpheus'
        assert response.json().get('job') == 'zion resident'

    def test_patch_update_user(self):
        response = self.base_api.patch(url=update_url, body=
        {
            "name": "morpheus2",
            "job": "zion resident2"
        })
        assert response.status_code == 200
        # Перевіряємо, що дані про користувача були оновлені
        assert response.json().get('name') == 'morpheus2'
        assert response.json().get('job') == 'zion resident2'

    def test_get_delayed_response(self):
        # Відправляємо запит GET з затримкою
        response = self.base_api.get(url=delayed_url)
        assert response.status_code == 200

        # Отримуємо список id з отриманих даних
        response_data = response.json()['data']
        response_ids = [user['id'] for user in response_data]
        # Очікуваний список id
        expected_ids = [1, 2, 3, 4, 5, 6]
        # Перевіряємо, що список id з отриманих даних співпадає з очікуваним списком id
        assert response_ids == expected_ids

    def test_delete_user(self):
        # Відправляємо запит DELETE для видалення користувача
        response = self.base_api.delete(url=update_url)
        # Перевіряємо, що відповідь має код статусу 204 (No Content), що означає успішне видалення
        assert response.status_code == 204

    def test_get_not_found(self):
        response = self.base_api.get(url=not_found)
        assert response.status_code == 404
