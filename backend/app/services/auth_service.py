from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data:dict):
    return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
