from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum
from pathlib import Path

app = FastAPI()

# Get the directory where the HTML/CSS files are located (same directory as this file)
BASE_DIR = Path(__file__).parent


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main index.html page"""
    html_path = BASE_DIR / "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


# Vercel serverless function handler
handler = Mangum(app)

