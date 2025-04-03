from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from typing_extensions import deprecated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])

security = HTTPBearer()

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

