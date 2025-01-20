class TokenDecodeError(Exception):
    def __init__(self):
        super().__init__("Not authenticated")


class AuthenticationError(Exception):
    def __init__(self):
        super().__init__("Not authenticated")


class AlreadyAuthenticatedError(Exception):
    def __init__(self):
        super().__init__("User already authenticated")


class AccessTokenError(Exception):
    def __init__(self):
        super().__init__("Token has expired or invalid")


class RefreshTokenError(Exception):
    def __init__(self):
        super().__init__("Refresh token has expired or invalid")
