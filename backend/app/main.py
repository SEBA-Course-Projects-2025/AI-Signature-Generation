from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
# import signature generator

app = FastAPI(
    title="Signature generator API",
    version="1.0",
)

class Generate_request(BaseModel):
    text: str


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
        "version": "Signature-model-v1.0"
    }
