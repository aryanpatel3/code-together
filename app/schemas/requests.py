from pydantic import BaseModel


class Submission(BaseModel):
    code: str
    problem_id: int
