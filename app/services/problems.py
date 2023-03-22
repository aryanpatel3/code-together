import json

from config import PROBLEMS_PATH


def get_problems():
    with open(PROBLEMS_PATH, 'r') as f:
        problems = json.load(f)

    return problems


def get_problem(problem_id: int):
    problems = get_problems()
    num_problems = len(problems["problems"])

    if problem_id <= 0 or problem_id > num_problems:
        return {"error": "Problem not found"}

    cur_problem = problems["problems"][problem_id - 1]

    starter_code_path = cur_problem["starter_code_path"]
    with open(starter_code_path, 'r') as f:
        starter_code = f.read()

    cur_problem["starter_code"] = starter_code

    return cur_problem
