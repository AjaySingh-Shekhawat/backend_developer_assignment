from email.policy import default
from sqlalchemy import Column,Integer,String
from app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True)
    password = Column(String)
    role = Column(Integer,default="user")
