from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12
)

def hash_password(password: str):
    return pwd_context.hash(password[:72])  # FIX bcrypt limit

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password[:72], hashed_password)