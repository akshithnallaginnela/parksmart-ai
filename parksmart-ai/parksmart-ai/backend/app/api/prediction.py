from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest, PredictionResponse
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/", response_model=PredictionResponse)
def predict(payload: PredictionRequest):
    now = datetime.utcnow()
    timestamps = []
    avail = []
    for i in range(0, payload.lookahead_minutes, 15):
        ts = (now + timedelta(minutes=i)).isoformat()
        timestamps.append(ts)
        avail.append(max(0, 5 - i//15))  # dummy decreasing availability
    return {"timestamps": timestamps, "available_spots": avail}
