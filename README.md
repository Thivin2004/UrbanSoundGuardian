**🎧 UrbanSound Guardian – AI Noise Monitoring Agent
**
A lightweight ML-powered AI agent that detects urban noise patterns, classifies sound types, evaluates severity, and recommends actions for authorities & citizens.
Features a simple FastAPI web interface + JSON API.

🚀 Overview

Urban environments generate continuous noise — traffic, construction, horns, emergency sirens.
Manual monitoring is impossible, and existing tools lack:

Real-time classification

Severity scoring

Actionable recommendations

AI-guided reasoning

UrbanSound Guardian solves this by combining:

A trained ML classifier

Rule-based severity engine

An intelligent AI agent wrapper

A simple FastAPI web application

Users can analyze any input audio filename (simulated), and the agent predicts:

Noise type

Noise score

Severity level

Recommended action

Citizen safety tips

🧠 How the Agent Works

The system has 3 core layers:

1️⃣ ML Model (Fake Synthetic Data-Based Classifier)

Trained on synthetic feature data (MFCC-like numeric vectors).
Predicts sound class probabilities for:

Traffic

Siren

Construction

Human noise

Engine noise

Outputs a noise score (0–100).

2️⃣ Severity & Recommendation Engine

Interprets model outputs to determine:

Severity Level: LOW / MEDIUM / HIGH

Authority Action: e.g., deploy inspectors, check regulations

Citizen Tip: e.g., avoid peak hours, use ear protection

3️⃣ AI Agent Wrapper (UrbanSoundAgent)

Provides:

Unified analyze() method

Timestamp

Location handling

Structured output format

🏗️ Architecture
         User Input (filename)
                  |
                  v
         FastAPI Web App
                  |
                  v
         UrbanSoundAgent
    ┌─────────────┬─────────────┐
    |             |             |
 ML Model   Severity Engine  Recommendation Engine
    |             |             |
    └─────────────┴─────────────┘
                  |
                  v
            Final Analysis JSON

🌐 Web App UI (FastAPI)

Simple interface:

Enter audio filename

Click Analyze

Receive structured result JSON

📸 UI Preview

(You can add screenshots later)

UrbanSound Guardian 🎧
Enter an audio file name and click analyze.

traffic.wav  [Analyze]

{
  "detected_sound": "construction",
  "noise_score": 88,
  "severity": "HIGH",
  ...
}

📦 Project Structure
UrbanSoundGuardian/
│
├── webapp.py               # FastAPI Web App
├── main.py                 # CLI entry (optional)
├── train.py                # ML training (synthetic)
├── model.pkl               # Saved trained model
├── requirements.txt        # Dependencies
│
├── urbansound/
│   ├── __init__.py
│   ├── agent.py            # UrbanSoundAgent logic
│   ├── model.py            # ML classifier
│   └── audio_features.py   # Synthetic feature extractor

🛠️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/UrbanSoundGuardian.git
cd UrbanSoundGuardian

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ (Optional) Retrain the model
python train.py

🚀 Run the Web App
uvicorn webapp:app --reload


Open browser:

UI → http://127.0.0.1:8000

API Docs → http://127.0.0.1:8000/docs

🔍 Example Output
{
  "location": "Unknown",
  "timestamp_utc": "2025-12-01T15:26:37.659669",
  "audio_file": "traffic.wav",
  "detected_sound": "construction",
  "noise_score": 88,
  "severity": "HIGH",
  "class_probabilities": [0.36, 0.11, 0.26, 0.13, 0.13],
  "recommended_action_for_authority": "Send city inspection team to check compliance with noise rules.",
  "recommended_tip_for_citizens": "Ensure construction follows permitted timings and uses noise barriers."
}

🎯 Key Features

✔ Lightweight ML classifier
✔ Severity scoring
✔ Action recommendation engine
✔ FastAPI web UI
✔ JSON API endpoint
✔ Timestamp & location support
✔ Easy to extend
✔ Submission-ready & resume-ready

📈 Future Enhancements

Real audio MFCC extraction

Deep learning model (CNN)

Real-time streaming input

Integration with IoT noise sensors

Dashboard for city authorities

Gemini-powered reasoning module

🏁 Conclusion

UrbanSound Guardian demonstrates how a compact AI agent can:

Analyze environmental noise

Score severity

Provide insights for public safety

Deliver results via a clean web interface
