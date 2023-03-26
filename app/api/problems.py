from fastapi import APIRouter

from services import problems
from errors import Error

router = APIRouter(
    prefix="/problems",
)


@router.get("")
async def fetch_all():
    data = problems.fetch_all()
    if isinstance(data, Error):
        return {"status": "error", "message": data}

    return {"status": "success", "data": data}

@router.get("/{problem_id}")
async def problem(problem_id: int):
    data = problems.fetch_one(problem_id)
    if isinstance(data, Error):
        return {"status": "error", "message": data}

    return {"status": "success", "data": data}
