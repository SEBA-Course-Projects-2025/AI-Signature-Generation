from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel
import logging
from logging_config import setup_logging
from prometheus_fastapi_instrumentator import Instrumentator
# import signature generator

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Signature generator API",
)


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


@app.get("/health")
def health_check():
    logger.info("Health check")
    return {"status": "ok"}


class Generate_request(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("frontend.html") as f:
        return f.read()


@app.post("/generate")
async def generate(request: Generate_request):
    if request.text.strip() == "":
        raise HTTPException(status_code=400, detail="Text input is empty")

    file_path = Path(__file__).resolve().parent / "test_image" / "image1.png"
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail=f"Image not found: {file_path}")

    try:
        # signature_image = function_call(request.text)
        return FileResponse(file_path, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
