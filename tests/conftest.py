import pytest

from api.order_api import OrderApi
from api.user_api import UserApi
from helpers.generators import generate_user_payload


@pytest.fixture
def user_api():
    return UserApi()


@pytest.fixture
def order_api():
    return OrderApi()


@pytest.fixture
def created_user(user_api):
    """Создаёт уникального пользователя и возвращает его данные + токен."""
    payload = generate_user_payload()
    response = user_api.create_user(payload)
    return {
        'payload': payload,
        'status_code': response['status_code'],
        'body': response['body'],
        'token': response['token'],
    }


@pytest.fixture
def registered_user_token(user_api):
    """Создаёт пользователя и возвращает токен, удаляя его после теста."""
    payload = generate_user_payload()
    response = user_api.create_user(payload)

    yield response['token']

    if response['token']:
        user_api.delete_user(response['token'])
