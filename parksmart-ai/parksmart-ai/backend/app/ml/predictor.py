import joblib, os
from typing import List
class ParkingPredictor:
    def __init__(self, model_path: str = "./ml_models/"):
        self.model_path = model_path
        self.rf_model = None
        self.scaler = None
        self.load_models()

    def load_models(self):
        # try to load models if present
        try:
            self.rf_model = joblib.load(os.path.join(self.model_path, "random_forest_model.pkl"))
        except Exception:
            self.rf_model = None

    def predict(self, features: List[float]):
        if self.rf_model:
            return self.rf_model.predict([features]).tolist()
        # fallback dummy prediction
        return [0]
