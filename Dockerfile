# 使用輕量級 Python 映像
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼
COPY . .

# Hugging Face 預設使用 7860 端口
EXPOSE 7860

# 啟動命令 (使用 uvicorn 跑 FastAPI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]