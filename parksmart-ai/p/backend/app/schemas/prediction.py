from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):
    parking_spot_id: int
    lookahead_minutes: int = 60

class PredictionResponse(BaseModel):
    timestamps: List[str]
    available_spots: List[int]
