import secrets

from pyston import PystonClient, File

from schemas.errors import ProblemError
from schemas.responses import Results
from services.problems import get_problem
from utils import create_input


async def execute_code(code, problem_id) -> Results:
    client = PystonClient()

    problem = get_problem(problem_id)

    if type(problem) is ProblemError:
        return Results(results="Problem not found")

    test_cases = problem['test_cases']
    stdin = create_input(problem)

    secret_hash = secrets.token_hex(32)

    with open(problem['execution_code_path'], 'r') as f:
        execution_code = f.read().replace("{STDOUT_PREFIX}", secret_hash)

    full_code = code + "\n\n" + execution_code

    output = await client.execute("python", [File(full_code)], stdin=stdin)

    if output.run_stage is None:
        return Results(results="Runtime Error")

    if output.run_stage.code != 0:
        return Results(results="Runtime Error")

    if output.run_stage.signal == "SIGKILL":
        return Results(results="Time Limit Exceeded")

    user_responses = [
        line.removeprefix(secret_hash + " ")
        for line in output.run_stage.output.split("\n")
        if line.startswith(secret_hash)
    ]

    if len(user_responses) != len(test_cases):
        return Results(results="Runtime Error")

    results = [
        test_case['expected_output'] == user_response
        for test_case, user_response in zip(
            test_cases,
            user_responses,
        )
    ]

    return Results(results=results)
