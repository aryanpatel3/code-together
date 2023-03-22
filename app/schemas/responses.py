from typing import List, Union

from pydantic import BaseModel


class TestCase(BaseModel):
    input: str
    expected_output: str


class Problem(BaseModel):
    title: str
    description: str
    test_cases: List[TestCase]
    starter_code: str


class Problems(BaseModel):
    problems: List[Problem]


class Results(BaseModel):
    results: Union[List[bool], str]
