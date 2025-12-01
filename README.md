# 🎧 UrbanSound Guardian – AI Noise Detection Agent

UrbanSound Guardian is an **AI-driven agent** that analyzes urban noise, classifies sound types, scores severity, and provides actionable recommendations.  
Built using **Python, FastAPI, and a lightweight ML model**, this project showcases a clean, production-ready AI agent workflow.


## 🚀 **Key Features**

- 🎯 **Sound type detection** (traffic, construction, sirens, machinery)
- 📊 **Noise severity classification** (Low / Medium / High)
- 🧠 **AI recommendations** for authorities & citizens
- 🌐 **FastAPI Web App + JSON API**
- 🕒 **Timestamp + location context**
- ⚡ **Fast, lightweight, and deployable anywhere**


## 🏗️ **Architecture Overview**


User Input (filename) ->FASTAPI Web App->UrbanSoundAgent->Final Analysis JSON Output


---

## 🛠️ **Installation**

1. Clone the repository
```bash
git clone https://github.com/Thivin2004/UrbanSoundGuardian.git
cd UrbanSoundGuardian


2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. (Optional) Retrain ML model
python train.py

🚀 **Run the Web App**
uvicorn webapp:app --reload


Open browser:

Web UI: http://127.0.0.1:8000

API Docs: http://127.0.0.1:8000/docs

🔍 **Example Output**
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

🎯 Why This Project Is Effective

✔ Clear ML pipeline (training → prediction → output)

✔ Agent-based reasoning layer

✔ FastAPI UI for clean demonstrations

✔ JSON endpoint for integrations

✔ Resume-ready real-world project

✔ Perfect for Google/Kaggle Agents Capstone

📈 Planned Improvements

🎵 Real audio MFCC feature extraction

🤖 CNN-based urban-sound classifier

📡 IoT noise sensor integration

📊 Live dashboard for authorities

🧠 Gemini-powered reasoning module

🏁 Conclusion

UrbanSound Guardian demonstrates how a compact AI agent can:

Analyze environmental noise

Classify severity

Provide meaningful insights

Assist authorities and citizens

Deliver results through a smooth web interface

It is simple, effective, deployable, and perfect for agent-based AI demonstrations.
