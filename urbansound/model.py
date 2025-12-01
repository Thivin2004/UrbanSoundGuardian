# urbansound/model.py

from typing import Tuple, List
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class UrbanSoundModel:
    """
    Wrapper around a RandomForest classifier for urban sound categories.
    """

    def __init__(self):
        # Fixed set of sound classes for this prototype
        self.classes: List[str] = ["traffic", "horn", "construction", "dogs", "crowd"]
        self.model: RandomForestClassifier | None = None

    def init_model(self) -> None:
        self.model = RandomForestClassifier(
            n_estimators=150,
            random_state=42,
            class_weight="balanced"
        )

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        if self.model is None:
            self.init_model()
        self.model.fit(X, y)

    def predict(self, features: np.ndarray) -> Tuple[str, List[float]]:
        if self.model is None:
            raise RuntimeError("Model not loaded or trained.")

        features = features.reshape(1, -1)
        label = self.model.predict(features)[0]
        proba = self.model.predict_proba(features)[0]
        return str(label), proba.tolist()

    def save(self, path: str = "model.pkl") -> None:
        if self.model is None:
            raise RuntimeError("Model not initialized.")
        payload = {
            "model": self.model,
            "classes": self.classes
        }
        joblib.dump(payload, path)

    @staticmethod
    def load(path: str = "model.pkl") -> "UrbanSoundModel":
        payload = joblib.load(path)
        inst = UrbanSoundModel()
        inst.model = payload["model"]
        inst.classes = payload["classes"]
        return inst
