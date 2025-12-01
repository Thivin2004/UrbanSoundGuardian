# main.py

from urbansound.agent import UrbanSoundAgent

def pretty_print(result: dict):
    print("\n====== UrbanSound Guardian – AI Agent Output ======")
    for key, value in result.items():
        print(f"{key}: {value}")
    print("===================================================\n")

if __name__ == "__main__":
    print("UrbanSound Guardian – Smart City Noise AI Agent")
    audio_file = input("Enter audio file name (e.g., traffic_demo.wav): ").strip()

    if not audio_file:
        audio_file = "traffic_demo.wav"  # default

    agent = UrbanSoundAgent(model_path="model.pkl")
    result = agent.analyze(audio_file, location="Sample Smart City Zone")
    pretty_print(result)
