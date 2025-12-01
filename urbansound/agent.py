# urbansound/agent.py

from typing import Dict, Any
import datetime

from .audio_features import get_features
from .model import UrbanSoundModel
from .rule_engine import noise_score_for_label, severity_from_score, recommended_actions

class UrbanSoundAgent:
    """
    UrbanSound Guardian AI Agent:
    - Perceives: audio file path
    - Thinks: extract features, run ML model, compute severity
    - Acts: produce recommended actions for authorities and citizens
    """

    def __init__(self, model_path: str = "model.pkl"):
        self.model = UrbanSoundModel.load(model_path)

    def analyze(self, audio_path: str, location: str = "Unknown Location") -> Dict[str, Any]:
        timestamp = datetime.datetime.utcnow().isoformat()

        # 1. Sense: extract features
        features = get_features(audio_path)

        # 2. Think: ML prediction
        predicted_label, probabilities = self.model.predict(features)

        # 3. Reason about impact
        score = noise_score_for_label(predicted_label)
        severity = severity_from_score(score)
        authority_action, citizen_tip = recommended_actions(predicted_label, severity)

        # 4. Act: return structured decision
        return {
            "location": location,
            "timestamp_utc": timestamp,
            "audio_file": audio_path,
            "detected_sound": predicted_label,
            "noise_score": score,
            "severity": severity,
            "class_probabilities": probabilities,
            "recommended_action_for_authority": authority_action,
            "recommended_tip_for_citizens": citizen_tip
        }
