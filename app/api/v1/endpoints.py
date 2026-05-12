# pyrefly: ignore [missing-import]
from fastapi import APIRouter, HTTPException
# pyrefly: ignore [missing-import]
from fastapi.responses import StreamingResponse, Response
from app.schemas.vcard_input import VCardJSONInput
from app.services.vcard_builder import build_vcard_from_json
from app.services.qr_service import generate_vcard_qr

router = APIRouter()

@router.post("/vcard/text", summary="回傳 vCard 字串")
async def generate_vcard_text(data: VCardJSONInput):
    try:
        vcard_text = build_vcard_from_json(data)
        return Response(content=vcard_text, media_type="text/vcard; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"處理失敗: {str(e)}")

@router.post("/vcard/qr", summary="回傳 vCard QR Code")
async def generate_vcard_qr_endpoint(data: VCardJSONInput):
    try:
        vcard_text = build_vcard_from_json(data)
        img_buf = generate_vcard_qr(vcard_text)
        return StreamingResponse(img_buf, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"處理失敗: {str(e)}")