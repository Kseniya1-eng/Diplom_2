import allure

from helpers.generators import generate_user_payload


@allure.story('Логин пользователя')
class TestLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self, user_api, created_user, registered_user_token):
        response = user_api.login_user(created_user['payload'])

        assert response['status_code'] == 200
        assert response['body']['success'] is True
        assert response['body']['user']['email'] == created_user['payload']['email']
        assert response['token'] is not None

    @allure.title('Логин с неверным логином и паролем')
    def test_login_wrong_credentials(self, user_api):
        payload = generate_user_payload()

        response = user_api.login_user(payload)

        assert response['status_code'] == 401
        assert response['body']['success'] is False
        assert response['body']['message'] == 'email or password are incorrect'
