from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class ParkingSpot(Base):
    __tablename__ = "parking_spots"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    total_spots = Column(Integer, nullable=False, default=0)
    available_spots = Column(Integer, nullable=False, default=0)
    price_per_hour = Column(Float, nullable=False, default=0.0)
    peak_price_per_hour = Column(Float, nullable=False, default=0.0)
    amenities = Column(JSON)
    is_active = Column(Boolean, default=True)
    rating = Column(Float, default=0.0)
    total_reviews = Column(Integer, default=0)
    owner_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ParkingOccupancy(Base):
    __tablename__ = "parking_occupancy"
    id = Column(Integer, primary_key=True, index=True)
    parking_spot_id = Column(Integer, index=True)
    occupied_spots = Column(Integer)
    available_spots = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    weather_condition = Column(String)
    temperature = Column(Float)
    is_peak_hour = Column(Boolean)
    nearby_events = Column(JSON)
