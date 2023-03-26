import secrets
from typing import Any, Union

from pyston import PystonClient, File

from errors import Error
from repositories import problems
from utils import create_input


async def execute_code(code: str, problem_id: int) -> Union[dict[str, Any], Error]:
    client = PystonClient()

    problem = problems.fetch_one(problem_id)
    if problem is None:
        return Error.PROBLEMS_NOT_FOUND

    test_cases = problem['test_cases']
    stdin = create_input(problem)

    secret_hash = secrets.token_hex(32)

    with open(problem['execution_code_path'], 'r') as f:
        execution_code = f.read().replace("{STDOUT_PREFIX}", secret_hash)

    full_code = code + "\n\n" + execution_code

    output = await client.execute("python", [File(full_code)], stdin=stdin)

    if output.run_stage is None:
        return Error.SUBMISSIONS_RUNTIME_ERROR

    if output.run_stage.code != 0:
        return Error.SUBMISSIONS_RUNTIME_ERROR

    if output.run_stage.signal == "SIGKILL":
        return Error.SUBMISSIONS_TIMEOUT

    user_responses = [
        line.removeprefix(secret_hash + " ")
        for line in output.run_stage.output.split("\n")
        if line.startswith(secret_hash)
    ]

    if len(user_responses) != len(test_cases):
        return Error.SUBMISSIONS_RUNTIME_ERROR

    results = [
        test_case['expected_output'] == user_response
        for test_case, user_response in zip(
            test_cases,
            user_responses,
        )
    ]

    return {"results": results}
