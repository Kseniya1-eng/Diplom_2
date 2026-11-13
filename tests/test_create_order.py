import allure

from helpers.generators import get_bun_id, get_sauce_id


@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth_and_ingredients(self, order_api, registered_user_token):
        payload = {'ingredients': [get_bun_id(), get_sauce_id()]}

        response = order_api.create_order(payload, token=registered_user_token)

        assert response['status_code'] == 200
        assert response['body']['success'] is True
        assert 'number' in response['body']['order']

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self, order_api):
        payload = {'ingredients': [get_bun_id()]}

        response = order_api.create_order(payload)

        assert response['status_code'] == 200
        assert response['body']['success'] is True
        assert 'number' in response['body']['order']

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredients(self, order_api, registered_user_token):
        payload = {'ingredients': [get_bun_id()]}

        response = order_api.create_order(payload, token=registered_user_token)

        assert response['status_code'] == 200
        assert response['body']['success'] is True
        assert len(response['body']['order']['ingredients']) > 0

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, order_api, registered_user_token):
        payload = {'ingredients': []}

        response = order_api.create_order(payload, token=registered_user_token)

        assert response['status_code'] == 400
        assert response['body']['success'] is False
        assert response['body']['message'] == 'Ingredient ids must be provided'

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash(self, order_api, registered_user_token):
        payload = {'ingredients': ['invalid_hash_12345']}

        response = order_api.create_order(payload, token=registered_user_token)

        assert response['status_code'] == 500
