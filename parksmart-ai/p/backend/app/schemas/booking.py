from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    user_id: int
    parking_spot_id: int
    start_time: datetime
    end_time: datetime

class BookingRead(BookingCreate):
    id: int
    total_price: float
    status: str
    class Config:
        orm_mode = True
