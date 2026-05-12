from app.schemas.vcard_input import VCardJSONInput

def build_vcard_from_json(data: VCardJSONInput) -> str:
    # 組合 ADR 字串
    adr_str = ";".join(data.adr)
    
    # 構建 vCard 3.0 格式 (使用 CRLF \r\n)
    vcard_lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{data.lastName};{data.firstName};;;",
        f"FN:{data.full_name}",
        f"ORG:{data.org}" if data.org else "",
        f"TITLE:{data.title}" if data.title else "",
        f"TEL;TYPE=WORK,VOICE:{data.tel_work}" if data.tel_work else "",
        f"TEL;TYPE=CELL:{data.tel_cell}" if data.tel_cell else "",
        f"EMAIL;TYPE=WORK,INTERNET:{data.email}" if data.email else "",
        f"ADR;TYPE=WORK:{adr_str}",
        f"NOTE:{data.note}" if data.note else "",
        f"URL:{data.url}" if data.url else "",
        "END:VCARD"
    ]
    
    # 過濾空行並合併
    return "\r\n".join([line for line in vcard_lines if line]) + "\r\n"