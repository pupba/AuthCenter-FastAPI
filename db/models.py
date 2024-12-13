from sqlalchemy import Column,Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    userid = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)  # default를 datetime.utcnow로 수정

    # User와 APIKey 간의 관계 설정
    api_keys = relationship("APIKey", back_populates="user")

class APIKey(Base):
    __tablename__ = "api_key"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'), nullable=False)
    api_key = Column(String, unique=True, default=lambda: str(uuid4()))  # default를 lambda로 수정
    created_at = Column(DateTime, default=datetime.now)  # default를 datetime.utcnow로 수정

    user = relationship("User", back_populates="api_keys")

