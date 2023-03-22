from pydantic import BaseModel


class ProblemError(BaseModel):
    error: str
