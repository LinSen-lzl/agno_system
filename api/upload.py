from fastapi import APIRouter, UploadFile, File
import uuid
from pathlib import Path

# 上传到该项目uploads目录下
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

upload_router = APIRouter(prefix="/api/upload", tags=["Upload"])

# 上传文件接口
@upload_router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_id = f"{uuid.uuid4()}.pdf"
    file_path = UPLOAD_DIR / file_id

    with open (file_path, "wb") as f:
        f.write(await file.read())

    return {
        "file_id": file_id,
        "file_path": str(file_path)
    }

