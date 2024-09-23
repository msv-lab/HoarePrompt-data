import subprocess


def execute_code(code_str: str, input_data: str):
    try:
        result = subprocess.run(['python3', '-c', code_str], input=input_data,
                                capture_output=True, text=True, timeout=3)
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return '', 'TimeoutError: Execution exceeded time limit'
    except Exception as e:
        return '', str(e)


def execute_tests(inputs, outputs, generated_code):
    passed_tests = 0
    total_tests = len(inputs)
    failure_example = None

    for input_data, expected_output in zip(inputs, outputs):
        stdout, stderr = execute_code(generated_code, input_data)

        if stderr:
            if failure_example is None:
                failure_example = {"input": input_data, "expected": expected_output, "got": stderr.strip()}
        else:
            if stdout.strip() == expected_output.strip():
                passed_tests += 1
            else:
                if failure_example is None:
                    failure_example = {"input": input_data, "expected": expected_output, "got": stdout.strip()}

    return passed_tests, total_tests, failure_example
