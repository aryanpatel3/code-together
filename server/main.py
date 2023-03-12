import json
import uvicorn

from pprint import pprint

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


@app.get("/problem")
async def get_problem():
    with open('sum_array.json', 'r') as f:
        problem = json.load(f)

    return problem


@app.post("/code")
async def run_code(request: RequestBody):
    client = PystonClient()

    with open('sum_array.json', 'r') as f:
        problem = json.load(f)

    test_cases = problem['test_cases']

    stdin = str(len(test_cases)) + "\n"
    for i in range(len(test_cases)):
        stdin += test_cases[i]['input'] + "\n"
    print("stdin:", stdin)

    output = await client.execute("python", [File(request.code)], stdin=stdin)

    if output.run_stage.code != 0:
        return {"results": "Runtime Error"}

    if output.run_stage.signal == "SIGKILL":
        return {"results": "Time Limit Exceeded"}

    pprint(output.run_stage.__dict__)

    results = []
    stdout = output.run_stage.output.split("\n")
    stdout.pop()
    print("stdout:", stdout)
    print("test_cases:", test_cases)

    for i in range(len(stdout)):
        results.append(stdout[i] == test_cases[i]['expected_output'])

    for i in range(len(test_cases) - len(stdout)):
        results.append(False)

    return {"results": results}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
