from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel
# import signature generator


app = FastAPI(
    title="Signature generator API",
)

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
