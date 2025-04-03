from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import hash_password, verify_password, create_access_token, get_current_user
from database import get_db
from models import User
from schemas import UserCreate, UserLogin

public_router = APIRouter()
private_router = APIRouter(dependencies=[Depends(get_current_user)])

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

@public_router.post("/users/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=404, detail="Incorrect password")

    access_token = create_access_token(data={"sub": db_user.username})

    return {"access_token": access_token, "token_type": "Bearer"}

@private_router.get("/protected")
async def protected_route():
    return {"message": "You are authorized to access this endpoint!"}