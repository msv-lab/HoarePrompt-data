import subprocess


def execute_code(code_str: str, input_data: str):
    try:
        result = subprocess.run(['python3', '-c', code_str], input=input_data,
                                capture_output=True, text=True, timeout=3)
        return result.stdout, result.stderr
    except Exception as e:
        return '', str(e)


def execute_tests(inputs, outputs, generated_code):
    passed_tests = 0
    total_tests = len(inputs)

    for input_data, expected_output in zip(inputs, outputs):
        stdout, stderr = execute_code(generated_code, input_data)

        if stderr:
            pass
            # print(f"Test case failed with error: {stderr}")
        else:
            if stdout.strip() == expected_output.strip():
                passed_tests += 1
            else:
                pass
                # print(f"Expected: {expected_output.strip()}, but got: {stdout.strip()}")

    return passed_tests, total_tests
