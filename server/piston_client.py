from pprint import pprint
from pyston import PystonClient, File


async def execute_python(code):
    client = PystonClient()
    output = await client.execute(
        "python", [File(code)]
    )

    pprint(output.run_stage.__dict__)

    if output.run_stage.code != 0:
        print("Runtime Error")

    if output.run_stage.signal == "SIGKILL":
        print("Time Limit Exceeded")

    return output.run_stage.output


async def execute_cplusplus(code):
    client = PystonClient()
    output = await client.execute("cpp", [File(code)])

    pprint(output.run_stage.__dict__)

    if output.compile_stage.code != 0:
        print("Compilation Error")

    if output.run_stage.code != 0:
        print("Runtime Error")

    if output.run_stage.signal == "SIGKILL":
        print("Time Limit Exceeded")

    return output.run_stage.output
