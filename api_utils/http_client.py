import requests
from config.settings import API_BASE_URL, API_TIMEOUT


class HttpClient:

    def __init__(self):
        self.base_url = API_BASE_URL

        # ✅ ADD HEADERS (THIS FIXES 403)
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            timeout=API_TIMEOUT
        )

    def post(self, endpoint, data):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=self.headers,
            timeout=API_TIMEOUT
        )