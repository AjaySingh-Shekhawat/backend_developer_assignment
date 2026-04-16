from sqlalchemy import Column, Integer,String
from app.database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    owner = Column(String)
