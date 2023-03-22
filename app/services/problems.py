import json
from typing import Union

from config import PROBLEMS_PATH
from schemas.errors import ProblemError
from schemas.responses import Problem, Problems


def get_problems() -> Problems:
    with open(PROBLEMS_PATH, 'r') as f:
        problems = json.load(f)

    return problems


def get_problem(problem_id: int) -> Union[Problem, ProblemError]:
    problems = get_problems()
    num_problems = len(problems["problems"])

    if problem_id <= 0 or problem_id > num_problems:
        return ProblemError(error="Problem not found")

    cur_problem: Problem = problems["problems"][problem_id - 1]

    starter_code_path = cur_problem["starter_code_path"]
    with open(starter_code_path, 'r') as f:
        starter_code = f.read()

    cur_problem["starter_code"] = starter_code

    return cur_problem
