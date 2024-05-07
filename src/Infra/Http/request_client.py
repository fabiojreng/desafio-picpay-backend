import requests
from src.Infra.Http.interface_client_http import HttpClientInterface


class RequestHttpClient(HttpClientInterface):
    def post(self, url: str, data: dict[str, any]):
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return e.response.json() if e.response else str(e)

    def get(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return {"status": response.status_code, "data": response.json()}
        except requests.exceptions.RequestException as e:
            return e.response.json() if e.response else str(e)
