import allure

from helpers.generators import generate_user_payload


@allure.story('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, user_api, created_user):
        assert created_user['status_code'] == 200
        assert created_user['body']['success'] is True
        assert created_user['body']['user']['email'] == created_user['payload']['email']
        assert created_user['body']['user']['name'] == created_user['payload']['name']
        assert created_user['token'] is not None

        # очистка созданного пользователя
        user_api.delete_user(created_user['token'])

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, user_api, created_user):
        assert created_user['status_code'] == 200

        duplicate_response = user_api.create_user(created_user['payload'])

        assert duplicate_response['status_code'] == 403
        assert duplicate_response['body']['success'] is False
        assert duplicate_response['body']['message'] == 'User already exists'

        user_api.delete_user(created_user['token'])

    @allure.title('Создание пользователя без одного из обязательных полей')
    def test_create_user_without_required_field(self, user_api):
        payload = generate_user_payload()
        del payload['name']

        response = user_api.create_user(payload)

        assert response['status_code'] == 403
        assert response['body']['success'] is False
        assert response['body']['message'] == 'Email, password and name are required fields'
