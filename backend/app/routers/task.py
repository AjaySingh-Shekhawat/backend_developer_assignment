from fastapi import HTTPException

from backend.app.database import SessionLocal
from backend.app.models.task import Task
from backend.app.routers.auth import router


@router.post("/tasks")
def create_task(title:str,description:str):
    db = SessionLocal()
    task = Task(title=title,description=description)
    db.add(task)
    db.commit()

    return task

@router.get("/tasks")
def get_task():
    db = SessionLocal()
    task = db.query(Task).all()
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    db = SessionLocal()
    task = db.qurery(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message":"Task Deleted"}


