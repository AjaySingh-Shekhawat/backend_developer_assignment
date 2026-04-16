from fastapi import FastAPI
from app.routers import auth, task
# from app.routes.auth import router
app = FastAPI()

app.include_router(auth.routers)
app.include_router(task.routers)
