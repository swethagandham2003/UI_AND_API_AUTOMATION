class AuthService:

    def login(self, email, password):
        # Fake success response
        class Response:
            status_code = 200

        return Response()