from api.client import StellarBurgersApi
from api.endpoints import CREATE_USER_ENDPOINT, LOGIN_ENDPOINT, USER_ENDPOINT


class UserApi(StellarBurgersApi):
    """Методы для работы с пользователями."""

    def create_user(self, payload: dict) -> dict:
        response = self.post(CREATE_USER_ENDPOINT, data=payload)
        return {
            'status_code': response.status_code,
            'body': response.json(),
            'token': response.json().get('accessToken'),
        }

    def login_user(self, payload: dict) -> dict:
        response = self.post(LOGIN_ENDPOINT, data=payload)
        return {
            'status_code': response.status_code,
            'body': response.json(),
            'token': response.json().get('accessToken'),
        }

    def delete_user(self, token: str) -> dict:
        response = self.delete(USER_ENDPOINT, token=token)
        return {
            'status_code': response.status_code,
            'body': response.json(),
        }
