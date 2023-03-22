def create_input(problem):
    test_cases = problem['test_cases']

    stdin = str(len(test_cases)) + "\n"
    for test_case in test_cases:
        stdin += test_case['input'] + "\n"

    return stdin
