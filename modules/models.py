from pydantic import BaseModel
from typing import Optional

class LoginResponse(BaseModel):
    username:str
    token:Optional[str] = None

class GetAPIKeyResponse(BaseModel):
    username:str
    apikey:Optional[str] = None

class APIKeyAuthResponse(BaseModel):
    username:str
    apikey:str
    success:bool