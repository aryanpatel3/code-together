from typing import Any, Union

from errors import Error
from repositories import problems


# NOTE: this can be expanded to support filtering & pagination
def fetch_all() -> Union[list[dict[str, Any]], Error]:
    data = problems.fetch_all()
    return data


def fetch_one(problem_id: int) -> Union[dict[str, Any], Error]:
    data = problems.fetch_one(problem_id)
    if data is None:
        return Error.PROBLEMS_NOT_FOUND

    return data
