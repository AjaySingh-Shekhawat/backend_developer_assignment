from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models.task import Task
from app.schemes.task import TaskCreate

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate):
    db = SessionLocal()
    try:
        new_task = Task(
            title=task.title,
            description=task.description
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task

    finally:
        db.close()


@router.get("/tasks")
def get_task():
    db = SessionLocal()
    try:
        return db.query(Task).all()
    finally:
        db.close()


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        db.delete(task)
        db.commit()

        return {"message": "Task Deleted"}

    finally:
        db.close()