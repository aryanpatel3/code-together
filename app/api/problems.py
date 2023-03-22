from typing import Union

from fastapi import APIRouter

from schemas.errors import ProblemError
from schemas.responses import Problems, Problem
from services.problems import get_problems, get_problem

router = APIRouter(
    prefix="/problems",
)


@router.get("")
async def problems() -> Problems:
    return get_problems()


@router.get("/{problem_id}")
async def problem(problem_id: int) -> Union[Problem, ProblemError]:
    return get_problem(problem_id)
