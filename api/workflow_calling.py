from fastapi import APIRouter, UploadFile, File
from fastapi import HTTPException
from pydantic import BaseModel
from workflows.doc_summary_workflow import doc_summary_workflow

# 工作流调用api
wc_router = APIRouter(prefix="/api/wc", tags=["WorkflowCalling"])

class DSResponse(BaseModel):
    answer: str

@wc_router.post("/docSummary", response_model=DSResponse)
async def docSummary(file: UploadFile = File(...)):
    try:
        content = await file.read()
        result = doc_summary_workflow.run(input=content)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


