# train.py

"""
Train a simple RandomForest classifier for urban noise types.

This uses synthetic/deterministic features generated from pseudo file names,
so it works even if you don't have real audio files yet.

Later, you can replace this with real UrbanSound-style data.
"""

import numpy as np

from urbansound.audio_features import get_features
from urbansound.model import UrbanSoundModel

def build_training_data():
    """
    Create a small synthetic dataset using fake file names.
    get_features() will either read audio if available or
    generate deterministic synthetic features.
    """
    label_to_files = {
        "traffic": [
            "data/traffic_mainroad_1.wav",
            "data/traffic_highway_2.wav",
            "data/traffic_junction_3.wav"
        ],
        "horn": [
            "data/horn_busy_junction_1.wav",
            "data/horn_peak_hour_2.wav",
            "data/horn_school_zone_3.wav"
        ],
        "construction": [
            "data/construction_site_1.wav",
            "data/construction_drilling_2.wav",
            "data/construction_hammer_3.wav"
        ],
        "dogs": [
            "data/dogs_barking_lane_1.wav",
            "data/dogs_stray_2.wav",
            "data/dogs_night_3.wav"
        ],
        "crowd": [
            "data/crowd_market_1.wav",
            "data/crowd_festival_2.wav",
            "data/crowd_mall_3.wav"
        ]
    }

    X_list = []
    y_list = []

    for label, files in label_to_files.items():
        for f in files:
            feat = get_features(f)
            X_list.append(feat)
            y_list.append(label)

    X = np.vstack(X_list)
    y = np.array(y_list)
    return X, y

if __name__ == "__main__":
    print("[INFO] Building training data...")
    X, y = build_training_data()
    print(f"[INFO] Training samples: {X.shape[0]}, feature dim: {X.shape[1]}")

    model = UrbanSoundModel()
    print("[INFO] Training model...")
    model.train(X, y)
    model.save("model.pkl")
    print("[INFO] Model saved as model.pkl")
