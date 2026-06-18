from fastapi import APIRouter
from fastapi.responses import JSONResponse

app_route = APIRouter(tags=["App"])

@app_route.get("/")
async def health():
    return JSONResponse(
        status_code= 200,
        content= {
            "message": "API rodando",
            "status": "online"
        }
    )

