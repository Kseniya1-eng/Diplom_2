import random
import string

import requests

from api.endpoints import BASE_URL, CREATE_ORDER_ENDPOINT


def generate_random_string(length: int = 8) -> str:
    """Генерирует случайную строку из букв и цифр."""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email() -> str:
    """Генерирует уникальный email для тестового пользователя."""
    return f'diplom_{generate_random_string(10)}@yandex.ru'


def generate_user_payload() -> dict:
    """Возвращает payload с уникальными данными пользователя."""
    return {
        'email': generate_unique_email(),
        'password': generate_random_string(10),
        'name': generate_random_string(6),
    }


def get_ingredient_id(ingredient_type: str = 'bun') -> str:
    """Возвращает id первого доступного ингредиента заданного типа."""
    response = requests.get(f'{BASE_URL}/api/ingredients')
    response.raise_for_status()
    ingredients = response.json()['data']
    for ingredient in ingredients:
        if ingredient['type'] == ingredient_type:
            return ingredient['_id']
    raise ValueError(f'Ингредиент типа {ingredient_type} не найден')


def get_bun_id() -> str:
    """Возвращает id булочки для создания заказа."""
    return get_ingredient_id('bun')


def get_sauce_id() -> str:
    """Возвращает id соуса для создания заказа."""
    return get_ingredient_id('sauce')


def create_order_request(payload: dict, token: str | None = None) -> requests.Response:
    """Отправляет запрос на создание заказа."""
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = token
    return requests.post(f'{BASE_URL}{CREATE_ORDER_ENDPOINT}', json=payload, headers=headers)
