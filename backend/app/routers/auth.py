from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password, verify_password
from app.services.auth_service import create_access_token
from app.schemes.user import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db = SessionLocal()
    try:
        new_user = User(
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User created successfully"}

    finally:
        db.close()


@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    try:
        db_user = db.query(User).filter(User.email == user.email).first()

        if not db_user or not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="Incorrect email or password")

        token = create_access_token({
            "sub": db_user.email,
            "role": db_user.role
        })

        return {"access_token": token, "token_type": "bearer"}

    finally:
        db.close()