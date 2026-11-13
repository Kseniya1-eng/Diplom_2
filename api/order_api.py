from api.client import StellarBurgersApi
from api.endpoints import CREATE_ORDER_ENDPOINT


class OrderApi(StellarBurgersApi):
    """Методы для работы с заказами."""

    def create_order(self, payload: dict, token: str | None = None) -> dict:
        response = self.post(CREATE_ORDER_ENDPOINT, data=payload, token=token)
        try:
            body = response.json()
        except ValueError:
            # сервис может вернуть не-JSON ответ (например, HTML при 500)
            body = {'raw': response.text}
        return {
            'status_code': response.status_code,
            'body': body,
        }
