from fastapi import APIRouter

from schemas.requests import Submission
from services.submissions import execute_code

router = APIRouter(
    prefix="/submissions",
)


@router.post("")
async def submit(request: Submission):
    results = await execute_code(request.code, request.problem_id)
    return results
