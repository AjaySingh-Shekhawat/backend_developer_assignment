from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=False)
    description = Column(String(500))
    owner = Column(String(255))