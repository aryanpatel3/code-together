from typing import Any

from repositories import problems
from errors import Error

# NOTE: this can be expanded to support filtering & pagination
def fetch_all() -> list[dict[str, Any]] | Error:
    data = problems.fetch_all()
    return data

def fetch_one(problem_id: int) -> dict[str, Any] | Error:
    data = problems.fetch_one(problem_id)
    if data is None:
        return Error.PROBLEMS_NOT_FOUND

    return data
