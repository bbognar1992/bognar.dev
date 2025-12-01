from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from mangum import Mangum
from pathlib import Path

app = FastAPI()

# Get the directory where the HTML/CSS files are located (parent directory of api/)
BASE_DIR = Path(__file__).parent.parent


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring and load balancers"""
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "bence.bognar.dev",
        },
        status_code=200
    )


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main index.html page"""
    html_path = BASE_DIR / "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


# Vercel serverless function handler
# Mangum needs to handle the ASGI app for Vercel's serverless environment
handler = Mangum(app, lifespan="off")

# Export handler for Vercel
__all__ = ["handler"]

