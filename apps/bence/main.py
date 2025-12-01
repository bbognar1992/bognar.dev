from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, Response
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).parent


@app.get("/health")
async def health_check():
    return JSONResponse(
        content={
            "status": "healthy",
        }
    )


@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_path = BASE_DIR / "html" / "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


# Serve CSS files from assets directory
@app.get("/assets/landing.css")
async def landing_css():
    return FileResponse(BASE_DIR / "assets" / "landing.css", media_type="text/css")


@app.get("/assets/styles.css")
async def styles_css():
    return FileResponse(BASE_DIR / "assets" / "styles.css", media_type="text/css")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True)