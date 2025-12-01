# webapp.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

try:
    from urbansound.agent import UrbanSoundAgent
except:
    from agent import UrbanSoundAgent

app = FastAPI(
    title="UrbanSound Guardian – Simple Web App",
    version="1.0",
)

agent = UrbanSoundAgent()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <body style="font-family:Arial; padding:30px;">
            <h1>UrbanSound Guardian 🎧</h1>
            <p>Enter an audio file name and click analyze.</p>
            
            <input id="fname" placeholder="traffic.wav" style="padding:8px; width:250px;" />
            <button onclick="analyze()" style="padding:8px;">Analyze</button>

            <pre id="out" style="margin-top:20px; background:#eee; padding:10px;"></pre>

            <script>
                async function analyze() {
                    let file = document.getElementById("fname").value;
                    let res = await fetch('/analyze?file=' + file);
                    let data = await res.json();
                    document.getElementById("out").innerText = JSON.stringify(data, null, 2);
                }
            </script>
        </body>
    </html>
    """

@app.get("/analyze")
async def analyze(file: str, location: str = "Unknown"):
    return agent.analyze(file, location=location)
