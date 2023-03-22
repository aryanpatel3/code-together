import json
from typing import Any

from config import PROBLEMS_PATH

def fetch_all() -> list[dict[str, Any]]:
    with open(PROBLEMS_PATH, 'r') as f:
        problems = json.load(f)

    return problems

def fetch_one(problem_id: int) -> dict[str, Any] | None:
    with open(PROBLEMS_PATH, 'r') as f:
        problems = json.load(f)

    if problem_id <= 0 or problem_id > len(problems["problems"]):
        return None

    problem = problems["problems"][problem_id - 1]

    # add starter code to the problem
    with open(problem["starter_code_path"], 'r') as f:
        problem["starter_code"] = f.read()

    return problem
