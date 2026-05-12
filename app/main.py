# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Request, status
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse
# pyrefly: ignore [missing-import]
from fastapi.exceptions import RequestValidationError
from app.api.v1.endpoints import router as v1_router

app = FastAPI(
    title="QR Service",
    description="高效能 vCard 轉 QR Code 服務",
    version="1.0.0"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        loc = " -> ".join([str(x) for x in error.get("loc", []) if x != "body"])
        msg = error.get("msg", "")
        err_type = error.get("type", "")
        
        if err_type == "missing":
            custom_msg = f"缺少必填欄位: {loc}"
        elif "value_error" in err_type:
            # Pydantic自訂驗證錯誤會拋出 value_error
            custom_msg = f"欄位內容錯誤: {loc} ({msg.replace('Value error, ', '')})"
        elif "type_error" in err_type:
            custom_msg = f"欄位格式錯誤: {loc} (請檢查資料型態)"
        else:
            custom_msg = f"欄位錯誤: {loc} ({msg})"
            
        errors.append(custom_msg)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": errors, "message": "輸入資料有誤，請檢查後再試。"}
    )

# 掛載版本化路由，未來可輕鬆擴充 v2
app.include_router(v1_router, prefix="/api/v1", tags=["V1"])

@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "alive", "message": "Vibe QR Service is running"}
# uvicorn app.main:app --reload 