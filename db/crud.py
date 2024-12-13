from db.models import User,APIKey
from sqlalchemy.orm import session
import hashlib
from typing import Callable
from uuid import uuid4

def encryption(text:str,method:Callable=hashlib.sha256)->str:
    hashed_data = method(text.encode()).hexdigest()
    return str(hashed_data)[:16]

# Create  User
def add_user(session:session.Session,user:User)->bool:
    try:
        session.add(user)
        # Create API Key
        session.add(APIKey(
            username=user.username,
        ))
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False
# User Read
def auth_user(session:session.Session,user_id:str,password:str)->bool | str:
    try:
        # user_id 검사
        user_id_hash = encryption(user_id)
        q = session.query(User).filter_by(userid=user_id_hash).with_entities(User.password,User.username).one_or_none()
        if q is None:
            raise Exception("사용자 없음")
        # password 검사
        password_hash = encryption(password)
        if password_hash != q[0]:
            raise Exception("비밀번호 틀림")
        return q[1]
    
    except Exception as e:
        session.rollback()
        return False
    
# API Key get
def get_APIKey(session:session.Session,username:str)->str | bool:
    try:
        q = session.query(APIKey).filter_by(username=username).with_entities(APIKey.api_key).one_or_none()
        if q is None:
            raise Exception("APIKey 없음")
        return q[0]
    except Exception as e:
        session.rollback()
        return False

# API Key auth
def auth_APIKey(session:session.Session,api_key:str,username:str)->bool:
    try:
        q = session.query(APIKey).filter_by(api_key=api_key).with_entities(APIKey.username).one_or_none()
        if q is None:
            raise Exception("올바르지 않은 APIKey")
        if q[0] != username:
            raise Exception("허락되지 않은 사용자")
        return True
    except Exception as e:
        session.rollback()
        return False

# Delete User and Key
def delete_user(session:session.Session,username:str)->bool:
    try:
        q = session.query(User).filter_by(username=username).one_or_none()
        if q is None:
            raise Exception("사용자 없음")
        
        api_key = session.query(APIKey).filter_by(username=q.username).one_or_none()
        
        if api_key is None:
            raise Exception("APIKey 없음")

        session.delete(q)
        session.delete(api_key)
        session.commit()
        return True
        

    except Exception as e:
        session.rollback()
        return False

def apiKey_update_all(session:session.Session)->bool:
    try:
        # 모든 APIKey를 업데이트
        q = session.query(APIKey).all()
        if q == []:
            raise Exception("APIKey 없음")
        for api_key in q:
            api_key.api_key = str(uuid4())

        session.commit()
        return True
    
    except Exception as e:
        session.rollback()
        return False

if __name__ == "__main__":
    pass
    from db.console import getSession

    cur = getSession()
    # add_user(cur,User(
    #     username="admin1",
    #     userid=encryption("admin1",hashlib.sha256),
    #     password=encryption("qwer1234!@",hashlib.sha256)
    # ))
    print(auth_user(cur,"admin1","qwer1234!@"))
    # auth_APIKey(cur,"34e53889-f1f7-4415-ab87-6fac408a00ae","admin1")
    # delete_user(cur,"admin1")
    # apiKey_update_all(cur)