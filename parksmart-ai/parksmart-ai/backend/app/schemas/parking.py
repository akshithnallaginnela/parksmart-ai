from pydantic import BaseModel
from typing import Optional

class ParkingSpotBase(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    total_spots: int
    price_per_hour: float

class ParkingSpotCreate(ParkingSpotBase):
    pass

class ParkingSpotRead(ParkingSpotBase):
    id: int
    available_spots: int
    class Config:
        orm_mode = True
