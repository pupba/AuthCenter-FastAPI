from sqlalchemy import create_engine
from db.models import User, APIKey
from sqlalchemy.orm import sessionmaker
import os

def getSession(URL:str="sqlite:///"):
    if "sqlite" in URL:
        temp = os.path.abspath("sqlite3_db_for_window/auth_center.sqlite")
        URL += temp
    engine = create_engine(URL)
    # Table Set
    User.metadata.create_all(engine)
    APIKey.metadata.create_all(engine)
    # # seesion
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ =="__main__":
    cur = getSession()