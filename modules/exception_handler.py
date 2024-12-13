from fastapi import HTTPException,status

class AuthenticationFailed(HTTPException):
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class TokenCreationFailed(HTTPException):
    def __init__(self, detail: str = "Token creation failed"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class APIKeyNotFound(HTTPException):
    def __init__(self, detail: str = "API Key not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class APIKeyAuthenticationFailed(HTTPException):
    def __init__(self, detail: str = "API Key Authentication Failed"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)