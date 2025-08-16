from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# import signature generator

app = FastAPI(
    title="Signature generator API",
    version="1.0",
)

class Generate_request(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("frontend.html") as f:
        return f.read()


@app.post("/generate")
async def generate(request: Generate_request):
    try:
        signature_image = 0 # function_call(request.text)
        return {"signature_image": signature_image}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/version")
async def version():
    return {
        "API": app.version,
        "version": "Signature-model-v1.1"
    }


class TriggerRequest(BaseModel):
    text: str

@app.post("/trigger")
def trigger_endpoint(request: TriggerRequest):
    filename = "test_image/image1.png"
    return FileResponse(filename, media_type="image/png")