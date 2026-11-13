import requests


class StellarBurgersApi:
    """Базовый клиент для работы с API Stellar Burgers."""

    def __init__(self):
        self.base_url = 'https://stellarburgers.education-services.ru'

    def _full_url(self, endpoint: str) -> str:
        return f'{self.base_url}{endpoint}'

    def post(self, endpoint: str, data: dict | None = None, token: str | None = None) -> requests.Response:
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = token
        return requests.post(self._full_url(endpoint), json=data, headers=headers)

    def delete(self, endpoint: str, token: str | None = None) -> requests.Response:
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = token
        return requests.delete(self._full_url(endpoint), headers=headers)
