from fastapi import APIRouter

from services.problems import get_problems, get_problem

router = APIRouter(
    prefix="/problems",
)


@router.get("")
async def problems():
    return get_problems()


@router.get("/{problem_id}")
async def problem(problem_id: int):
    return get_problem(problem_id)
