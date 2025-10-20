from fastapi import APIRouter, Depends
from app.schemas.booking import BookingCreate, BookingRead
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=BookingRead)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    # placeholder booking computation
    duration = (payload.end_time - payload.start_time).total_seconds() / 3600.0
    return {"id": 1, "user_id": payload.user_id, "parking_spot_id": payload.parking_spot_id, "start_time": payload.start_time, "end_time": payload.end_time, "total_price": duration*10.0, "status": "confirmed"}
