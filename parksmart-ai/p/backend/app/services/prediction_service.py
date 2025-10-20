from app.ml.predictor import ParkingPredictor
predictor = ParkingPredictor()

def get_prediction(parking_spot_id: int, minutes: int = 60):
    return predictor.predict([parking_spot_id, minutes])
