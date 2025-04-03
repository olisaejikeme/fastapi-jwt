from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth import hash_password
from database import get_db
from models import User
from schemas import UserCreate

public_router = APIRouter()

@public_router.post("/users/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User (
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User has been created successfully", "user_id": new_user.id}
