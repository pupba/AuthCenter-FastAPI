from fastapi import APIRouter,Depends,Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from modules.models import GetAPIKeyResponse,APIKeyAuthResponse
from modules.exception_handler import TokenCreationFailed,APIKeyNotFound,APIKeyAuthenticationFailed
# db
from db.console import getSession
from db.crud import auth_APIKey,get_APIKey
# auth
from modules.jwt import auth_jwt_token


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get-api-key",response_model=GetAPIKeyResponse)
async def getAPIKey(token:str=Depends(oauth2_scheme)):
    # Token 인증
    auth_data = auth_jwt_token(token=token)
    if isinstance(auth_data,bool):
        raise TokenCreationFailed("Token 인증 실패")
    
    cur = getSession()

    api_key = get_APIKey(cur,auth_data)
    cur.close()

    if isinstance(api_key,bool):
        return APIKeyNotFound
    
    return GetAPIKeyResponse(username=auth_data,apikey=api_key)


@router.post("/auth-api-key",response_model=APIKeyAuthResponse)
async def authAPIKey(
    api_key:str=Form(...),
    username:str=Form(...)
    ):
    # APIKey 인증
    cur = getSession()
    if auth_APIKey(cur,api_key,username):
        cur.close()
        return APIKeyAuthResponse(username=username,apikey=api_key,success=True)
    else:
        cur.close()
        raise APIKeyAuthenticationFailed("API Key 인증 실패")