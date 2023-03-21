#!/usr/bin/env python3
import json
import uvicorn
import secrets

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from pyston import PystonClient, File

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


class RequestBody(BaseModel):
    code: str
    problem_id: int


@app.get("/problems")
async def get_problems():
    with open('problems.json', 'r') as f:
        problems = json.load(f)

    return problems


@app.get("/problems/{problem_id}")
async def get_problem(problem_id: int):
    problems = await get_problems()
    num_problems = len(problems["problems"])

    if problem_id <= 0 or problem_id > num_problems:
        return {"error": "Problem not found"}

    return problems["problems"][problem_id - 1]


def create_input(problem):
    test_cases = problem['test_cases']

    stdin = str(len(test_cases)) + "\n"
    for test_case in test_cases:
        stdin += test_case['input'] + "\n"

    return stdin

@app.post("/code")
async def run_code(request: RequestBody):
    client = PystonClient()

    problem = await get_problem(request.problem_id)

    test_cases = problem['test_cases']
    stdin = create_input(problem)

    secret_hash = secrets.token_hex(32)

    with open(problem['execution_code_path'], 'r') as f:
        execution_code = f.read().replace("{STDOUT_PREFIX}", secret_hash)

    full_code = request.code + "\n\n" + execution_code

    output = await client.execute("python", [File(full_code)], stdin=stdin)

    if output.run_stage is None:
        return {"results": "Runtime Error"}

    if output.run_stage.code != 0:
        return {"results": "Runtime Error"}

    if output.run_stage.signal == "SIGKILL":
        return {"results": "Time Limit Exceeded"}

    user_responses = [
        line.removeprefix(secret_hash + " ")
        for line in output.run_stage.output.split("\n")
        if line.startswith(secret_hash)
    ]

    results = [
        test_case['expected_output'] == user_response
        for test_case, user_response in zip(
            test_cases,
            user_responses,
            strict=True,
        )
    ]

    return {"results": results}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
