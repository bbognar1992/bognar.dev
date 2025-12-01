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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True)