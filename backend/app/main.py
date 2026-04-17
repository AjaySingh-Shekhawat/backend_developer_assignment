from fastapi import FastAPI
from app.database import Base, engine
from app.routers.auth import router as auth_router
from app.routers.task import router as task_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(task_router)