from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.parking import ParkingSpotCreate, ParkingSpotRead
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[ParkingSpotRead])
def list_parking(db: Session = Depends(get_db)):
    # return empty list as placeholder
    return []

@router.post("/", response_model=ParkingSpotRead)
def create_parking(payload: ParkingSpotCreate, db: Session = Depends(get_db)):
    return {**payload.dict(), "id": 1, "available_spots": payload.total_spots}
