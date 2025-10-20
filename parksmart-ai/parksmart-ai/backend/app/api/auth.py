from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # minimal example: hash password and return user-like object (not persisted)
    hashed = pwd_context.hash(user.password)
    return {"id": 1, "email": user.email, "full_name": user.full_name, "is_active": True}
