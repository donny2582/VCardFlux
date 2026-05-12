import segno
import io

def generate_vcard_qr(vcf_text: str, scale: int = 10) -> io.BytesIO:
    # 1. 格式清洗 (Vibe Optimization)
    # 確保換行符號為 CRLF (\r\n)，這是手機通訊錄識別的關鍵標準
    lines = [line.strip() for line in vcf_text.splitlines() if line.strip()]
    clean_vcf = "\r\n".join(lines) + "\r\n"

    # 2. 生成 QR Code (使用 M 等級糾錯，兼顧容量與掃描率)
    qr = segno.make(clean_vcf, error='m')
    
    # 3. 轉化為圖片流
    buf = io.BytesIO()
    # dark='#1a73e8' 為 Google 藍，可依需求更改
    qr.save(buf, kind='png', scale=scale, dark='#000000', light='#ffffff')
    buf.seek(0)
    return buf