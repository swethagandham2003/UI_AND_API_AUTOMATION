from api_utils.http_client import HttpClient


class UserService:

    def __init__(self):
        self.client = HttpClient()

    def get_users(self):
        return self.client.get("/users")

    def create_user(self, name, job):
        return self.client.post("/posts", {
            "title": name,
            "body": job,
            "userId": 1
        })