from enum import Enum


class Error(str, Enum):
    PROBLEMS_NOT_FOUND = "problems.not_found"

    SUBMISSIONS_RUNTIME_ERROR = "code_submission.error"
    SUBMISSIONS_TIMEOUT = "code_submission.timeout"
