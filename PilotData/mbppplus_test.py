import subprocess


def execute_code(code_str: str):
    try:
        result = subprocess.run(['python3', '-c', code_str], capture_output=True,
                                text=True, timeout=3)
        return result.stdout, result.stderr
    except Exception as e:
        return '', str(e)


def execute_test(code: str, test: str):
    test_code = code + '\n' + test
    _, err = execute_code(test_code)
    if err:
        return False, {'test': test, 'error': err.strip()}
    else:
        return True, {'test': test, 'status': 'Passed'}


def execute_tests(item: dict, code: str):
    assertions = item.get('assertion', '')
    item_results = {'task_id': item.get('task_id', ''), 'tests': [], 'errors': []}
    passed_tests = 0
    total_tests = 0

    for test in assertions.strip().split('\n'):
        if test.strip():
            total_tests += 1
            ok, res = execute_test(code, test)
            if ok:
                passed_tests += 1
                item_results['tests'].append(res)
            else:
                item_results['errors'].append(res)

    return total_tests, passed_tests, item_results


def summary(passed_tests: int, total_tests: int) -> float:
    pass_rate = passed_tests / total_tests if total_tests else 0
    return pass_rate


