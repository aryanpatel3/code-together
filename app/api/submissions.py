from fastapi import APIRouter

from schemas.requests import Submission
from schemas.responses import Results
from services.submissions import execute_code

router = APIRouter(
    prefix="/submissions",
)


@router.post("")
async def submit(request: Submission) -> Results:
    results = await execute_code(request.code, request.problem_id)
    return results
