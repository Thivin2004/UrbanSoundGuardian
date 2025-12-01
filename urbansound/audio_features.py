# urbansound/audio_features.py

import os
import hashlib
import numpy as np
import librosa

def _deterministic_random_vector(key: str, size: int = 40) -> np.ndarray:
    """
    Generate a deterministic random vector based on a string key.
    This ensures consistent features for the same file name,
    even if the audio file does not actually exist.
    """
    h = hashlib.md5(key.encode("utf-8")).hexdigest()
    seed = int(h, 16) % (2**32)
    rng = np.random.RandomState(seed)
    return rng.randn(size)

def get_features(audio_path: str) -> np.ndarray:
    """
    Extract MFCC-based features from an audio file if it exists.
    If the file does NOT exist or fails to load, generate a deterministic
    synthetic feature vector instead.

    This makes the project runnable even without real audio files,
    and allows you to plug in real .wav files later.
    """
    if os.path.exists(audio_path):
        try:
            y, sr = librosa.load(audio_path, sr=None)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
            mfcc_mean = mfcc.mean(axis=1)
            mfcc_std = mfcc.std(axis=1)
            features = np.concatenate([mfcc_mean, mfcc_std], axis=0)  # 40-dim
            return features
        except Exception as e:
            print(f"[WARN] Failed to read audio '{audio_path}': {e}")

    # Fallback: deterministic synthetic features based on file path
    return _deterministic_random_vector(audio_path, size=40)
