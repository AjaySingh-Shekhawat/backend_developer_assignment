from fastapi import APIRouter,Depends,HTTPException
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password,verify_password
from app.services.auth_service import create_access_token
from jinja2.runtime import identity

router = APIRouter()

@router.post("/register")
def register(email:str,password:str):
    db = SessionLocal()

    user = User(email=email,password=hash_password(password))
    db.add(user)
    db.commit()

    return {"message":"User created Successfully"}

@router.post("/login")
def login(email:str,password:str):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password,user.password):
        raise HTTPException(status_code=401,detail="Incorrect email or password")
    token = create_access_token({"sub":user.email,"role":user.role})
    return {"access_token":token,"token_type":"bearer"}
