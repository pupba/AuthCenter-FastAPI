from jose import JWTError, jwt
from datetime import datetime,timedelta
# JWT 설정
from orjson import loads
import os

# JWT Token 생성
def create_jwt_token(data:dict,expires_delta:timedelta=timedelta(minutes=60))->str | None:
    # Secret
    try:
        with open(os.path.abspath("secret.json"),"rb+") as f:
            secret = loads(f.read())
    except FileNotFoundError as e:
        print("Setting 파일(secret.json) 없음")
        return None
    to_encode = data.copy()
 
    expire = datetime.now() + expires_delta # 유효 시간(기본 60분) 

    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,secret['SECRET_KEY'],algorithm=secret['ALGORITHM'])
    return encoded_jwt

def auth_jwt_token(token:str)->str | bool:
    try:
        with open(os.path.abspath("secret.json"),"rb+") as f:
            secret = loads(f.read())

        payload = jwt.decode(token,secret['SECRET_KEY'],algorithms=secret['ALGORITHM'])
        username:str = payload.get('sub')
        if username is None:
            print("정보 없음")
            return False
        
        return username
    except FileNotFoundError as e:
        print("Setting 파일(secret.json) 없음")
        return False
    
    except JWTError as e:
        print(f"{e}")
        return False
    

# if __name__ == "__main__":
    # data = {"sub":"admin1"}

    # token = create_jwt_token(data)
    # print(auth_jwt_token(token="dasdasfsa"))