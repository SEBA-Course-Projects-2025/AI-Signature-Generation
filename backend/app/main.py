from tkinter import Image

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel
import logging
from logging_config import setup_logging
from prometheus_fastapi_instrumentator import Instrumentator
import requests
import base64
from PIL import Image
from io import BytesIO
# import signature generator

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Signature generator API",
)
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

    url = "https://90ab3535f32f.ngrok-free.app/generate"
    payload = {
        "name": request.text.strip()
    }

    res = requests.post(url, json=payload)
    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    data = res.json()
    img_base64 = data["img_base64"]
    image = Image.open(BytesIO(base64.b64decode(img_base64)))

    try:
        # signature_image = function_call(request.text)
        return FileResponse(image, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
