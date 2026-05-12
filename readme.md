# Vibe QR Service

Vibe QR Service 是一個基於 FastAPI 構建的高效能服務，專門用於將結構化的聯絡人資料（JSON）轉換為標準的 vCard 格式，並進一步生成高解析度的 QR Code 圖片。

## 核心功能 (Features)

- **自動生成 vCard 格式**：將前端傳入的 JSON 結構自動轉換為標準的 vCard 3.0/4.0 格式字串。
- **QR Code 圖片生成**：支援將生成的 vCard 字串轉換為包含完整聯絡資訊的 QR Code (PNG 格式)。
- **資料驗證與模型化**：透過 `Pydantic` 進行嚴謹的輸入資料驗證，確保資料的一致性與正確性。
- **高效能 API**：基於 `FastAPI` 框架開發，具備非同步處理能力，適合高併發場景。

## 系統架構 (Architecture)

專案採用分層架構，確保高內聚與低耦合：

```text
vcard-qr-service/
├── .venv/                  # 虛擬環境 (Git Ignored)
├── app/
│   ├── main.py             # 應用程式入口與 FastAPI 實例配置
│   ├── api/
│   │   └── v1/             # API 路由版本化管理
│   │       └── endpoints.py # 定義所有的 HTTP API 端點
│   ├── schemas/            # Pydantic 資料模型與驗證邏輯
│   │   └── vcard_input.py
│   └── services/           # 核心業務邏輯
│       ├── vcard_builder.py # JSON 轉 vCard 邏輯
│       └── qr_service.py   # QR Code 圖片生成邏輯
├── requirements.txt        # 專案套件依賴清單
└── Dockerfile              # 容器化部署規格
```

## API 端點 (API Endpoints)

服務運行後，您可以訪問 `/docs` 或 `/redoc` 查看完整的 Swagger UI 互動式技術文件。

目前的 API 端點（位於 `/api/v1` 前綴下）包含：

1. **`POST /api/v1/vcard/text`**
   - **描述**：將 JSON 資料轉換為標準 vCard 字串。
   - **回傳**：`text/vcard; charset=utf-8` 格式的字串。

2. **`POST /api/v1/vcard/qr`**
   - **描述**：將 JSON 資料轉換為 vCard QR Code 圖片。
   - **回傳**：`image/png` 格式的圖片串流。

## 本地開發與運行 (Local Development)

### 1. 環境需求
- Python 3.9+
- 建議使用虛擬環境隔離依賴套件

### 2. 環境建立與依賴安裝

```bash
# 建立虛擬環境
python -m venv .venv

# 啟動虛擬環境 (Windows)
.\.venv\Scripts\activate
# 啟動虛擬環境 (macOS/Linux)
source .venv/bin/activate

# 安裝依賴套件
pip install -r requirements.txt
```

*(註：核心套件包含 FastAPI, Uvicorn, Segno, Pydantic 等)*

### 3. 啟動服務

使用 Uvicorn 啟動 FastAPI 開發伺服器（預設運行於 port 8000）：

```bash
uvicorn app.main:app --reload
```

啟動後，請開啟瀏覽器前往：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 以進行 API 測試。

## 部署配置 (Deployment)

專案包含標準的 `Dockerfile`，可輕易部署至各式容器化環境 (如 Docker, Kubernetes, AWS ECS, GCP Cloud Run)。

```bash
# 構建 Docker 映像檔
docker build -t vibe-qr-service .

# 運行容器 (於背景執行並映射 8000 埠)
docker run -d -p 8000:8000 vibe-qr-service
```
