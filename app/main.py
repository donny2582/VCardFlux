# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router

app = FastAPI(
    title="QR Service",
    description="高效能 vCard 轉 QR Code 服務",
    version="1.0.0"
)

# 掛載版本化路由，未來可輕鬆擴充 v2
app.include_router(v1_router, prefix="/api/v1", tags=["V1"])

@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "alive", "message": "Vibe QR Service is running"}