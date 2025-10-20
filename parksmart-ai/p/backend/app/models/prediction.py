from sqlalchemy import Column, Integer, JSON, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    parking_spot_id = Column(Integer)
    result = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
