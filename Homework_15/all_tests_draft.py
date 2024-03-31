
#створювала собі чорновик

import requests  # Доданий імпорт модулю requests

base_url = 'https://reqres.in'
users_url = f'{base_url}/api/users'
# Оголошуємо URL для оновлення користувача
update_url = f'{base_url}/api/users/2'
# Оголошуємо URL для перевірки списку користувачів на 2 сторінці
list_users = f'{base_url}/api/users?page=2'
# Успішне залогінення
login_successful = f'{base_url}/api/login'
# Затримка відповіді
delayed_url = f'{base_url}/api/users?delay=3'
# Реєстрація
register_successful = f'{base_url}/api/register'
#Не існує сторінки
not_found = f'{base_url}/unknown/23'


def test_post_register_successful():
    response = requests.post(url=register_successful, data=
    {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    assert response.status_code == 200
    # Перевіряємо, що відповідь містить ключ 'id' та 'token'
    assert 'id' in response.json()
    assert 'token' in response.json()

    # Додатково перевіряємо, чи є значення 'id' та 'token' непорожніми рядками
    assert response.json()['id'] != ''
    assert response.json()['token'] != ''


def test_post_register_unsuccessful():
    response = requests.post(url=register_successful, data=
    {
        "email": "sydney@fife"
    })
    assert response.status_code == 400
    assert 'error' in response.json()  # Перевіряємо, що відповідь містить error
     # Додатково чи є error непорожнім рядком
    assert response.json()['error'] != ''


def test_post_login_successful():
    response = requests.post(url=login_successful, data=
    {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })
    assert response.status_code == 200
    assert 'token' in response.json()  # Перевіряємо, що відповідь містить токен
 # Додатково можна перевірити, чи є токен непорожнім рядком
    assert response.json()['token'] != ''


def test_post_login_unsuccessful():
    response = requests.post(url=login_successful, data=
    {
        "email": "peter@klaven"
    })
    assert response.status_code == 400
    assert 'error' in response.json()  # Перевіряємо, що відповідь містить error
     # Додатково чи є error непорожнім рядком
    assert response.json()['error'] != ''


def test_get_all_users_are_unique():
    response = requests.get(url=users_url)
    assert response.status_code == 200
    ids = [k['id'] for k in response.json()['data']]
    assert len(set(ids)) == len(ids)


def test_get_list_users():
    response = requests.get(url=list_users)
    assert response.status_code == 200
    ids = [k['id'] for k in response.json()['data']]
    assert len(set(ids)) == len(ids)


def test_post_create_user():
    response = requests.post(url=users_url, data=
    {
        "name": "morpheus",
        "job": "leader"
    })
    assert response.status_code == 201
    assert response.json().get('id')


def test_put_update_user():
    response = requests.put(url=update_url, json=
    {
        "name": "morpheus",
        "job": "zion resident"
    })
    assert response.status_code == 200

    # Перевіряємо, що дані про користувача були оновлені
    assert response.json().get('name') == 'morpheus'
    assert response.json().get('job') == 'zion resident'


test_put_update_user()


def test_patch_update_user():
    response = requests.patch(url=update_url, json=
    {
        "name": "morpheus2",
        "job": "zion resident2"
    })
    assert response.status_code == 200

    # Перевіряємо, що дані про користувача були оновлені
    assert response.json().get('name') == 'morpheus2'
    assert response.json().get('job') == 'zion resident2'


test_patch_update_user()


def test_get_delayed_response():
    # Відправляємо запит GET з затримкою
    response = requests.get(url=delayed_url)
    assert response.status_code == 200

    # Отримуємо список id з отриманих даних
    response_data = response.json()['data']
    response_ids = [user['id'] for user in response_data]
    # Очікуваний список id
    expected_ids = [1, 2, 3, 4, 5, 6]
    # Перевіряємо, що список id з отриманих даних співпадає з очікуваним списком id
    assert response_ids == expected_ids


test_get_delayed_response()


def test_delete_user():
    # Відправляємо запит DELETE для видалення користувача
    response = requests.delete(url=update_url)
    # Перевіряємо, що відповідь має код статусу 204 (No Content), що означає успішне видалення
    assert response.status_code == 204


def test_get_not_found():
    response = requests.get(url=not_found)
    assert response.status_code == 404