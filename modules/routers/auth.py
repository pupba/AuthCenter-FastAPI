from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# model
from modules.models import LoginResponse
# exception
from modules.exception_handler import AuthenticationFailed,TokenCreationFailed
# db
from db.console import getSession
from db.crud import auth_user
# from db.models import User,APIKey
# JWT
from modules.jwt import create_jwt_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login",response_model=LoginResponse)
async def login(
    form_data:OAuth2PasswordRequestForm = Depends()
):
    db = getSession() # 세선 만들기
    result = auth_user(db,form_data.username,form_data.password) # 사용자 인증
    if isinstance(result,bool):
        raise AuthenticationFailed("사용자 인증 실패")
    db.close() # 세션 종료

    # Token 생성
    token = create_jwt_token(data={'sub':result})
    if isinstance(token,bool):
        raise TokenCreationFailed("Token 생성 실패")
    
    return LoginResponse(username=result,token=token) # 성공