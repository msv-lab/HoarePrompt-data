import subprocess
import re


def execute_code(code_str: str):
    try:
        result = subprocess.run(['python3', '-c', code_str],
                                capture_output=True, text=True, timeout=3)
        return result.stdout, result.stderr
    except Exception as e:
        return '', str(e)


def clean_output(output):
    return re.sub(r'\s+', ' ', output.strip())


def safe_eval(output, expected_output):
    try:
        return eval(output) == eval(expected_output)
    except Exception as e:
        print(f"Eval error: {e}")
        return False


def test_function(task, generated_code):
    base_input = task['base_input']
    plus_input = task['plus_input']
    entry_point = task['entry_point']
    reference_code = task['canonical_solution']
    assertion_tests = task.get('assertion', '').splitlines()

    base_correct = 0
    for i, inputs in enumerate(base_input):
        base_ref_code = f"""
{reference_code}
result = {entry_point}(*{inputs})
print(result)
"""
        base_ref_output, base_ref_error = execute_code(base_ref_code)
        base_ref_output_clean = clean_output(base_ref_output) if not base_ref_error else ""

        base_test_code = f"""
{generated_code}
result = {entry_point}(*{inputs})
print(result)
"""
        base_output, base_error = execute_code(base_test_code)
        base_output_clean = clean_output(base_output) if not base_error else ""

        if safe_eval(base_output_clean, base_ref_output_clean):
            print(f"Base test case {i + 1} passed.")
            base_correct += 1
        else:
            print(f"Base test case {i + 1} failed: expected {base_ref_output_clean}, got {base_output_clean}")

    base_accuracy = base_correct / len(base_input) if base_input else 0

    plus_correct = 0
    for i, inputs in enumerate(plus_input):
        plus_ref_code = f"""
{reference_code}
result = {entry_point}(*{inputs})
print(result)
"""
        plus_ref_output, plus_ref_error = execute_code(plus_ref_code)
        plus_ref_output_clean = clean_output(plus_ref_output) if not plus_ref_error else ""

        plus_test_code = f"""
{generated_code}
result = {entry_point}(*{inputs})
print(result)
"""
        plus_output, plus_error = execute_code(plus_test_code)
        plus_output_clean = clean_output(plus_output) if not plus_error else ""

        if safe_eval(plus_output_clean, plus_ref_output_clean):
            print(f"Plus test case {i + 1} passed.")
            plus_correct += 1
        else:
            print(f"Plus test case {i + 1} failed: expected {plus_ref_output_clean}, got {plus_output_clean}")

    plus_accuracy = plus_correct / len(plus_input) if plus_input else 0

    assertion_success_count = 0
    total_assertion_tests = len(assertion_tests)
    for i, assertion_test in enumerate(assertion_tests):
        assertion_test_code = f"""
{generated_code}

{assertion_test}
"""
        assertion_output, assertion_error = execute_code(assertion_test_code)

        if assertion_error:
            print(f"Assertion test {i + 1} failed: {assertion_error}")
        else:
            assertion_success_count += 1
            print(f"Assertion test {i + 1} passed.")

    assertion_accuracy = assertion_success_count / total_assertion_tests if total_assertion_tests > 0 else 0

    print(f"Base input accuracy: {base_accuracy * 100:.2f}%")
    print(f"Plus input accuracy: {plus_accuracy * 100:.2f}%")
    print(f"Assertion tests passed {assertion_success_count}/{total_assertion_tests}")
    return base_accuracy, plus_accuracy, assertion_accuracy


if __name__ == "__main__":
    task = {
        "task_id": "Mbpp/2",
        "prompt": "\"\"\"\nWrite a function to find the shared elements from the given two lists.\nassert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))\n\"\"\"\n",
        "entry_point": "similar_elements",
        "canonical_solution": "def similar_elements(test_tup1, test_tup2):\n  return tuple(set(test_tup1) & set(test_tup2))\n",
        "base_input": [[[3, 4, 5, 6], [5, 7, 4, 10]], [[1, 2, 3, 4], [5, 4, 3, 7]],
                       [[11, 12, 14, 13], [17, 15, 14, 13]]],
        "plus_input": [[[], []], [[1, 2, 3], []], [[], [4, 5, 6]],
                       [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]],
        "assertion": "assert similar_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)\nassert similar_elements((1, 2, 3, 4), (5, 4, 3, 7)) == (3, 4)\n"
    }

    generated_code = """
def similar_elements(test_tup1, test_tup2):
    return tuple(set(test_tup1) & set(test_tup2))
"""

    base_accuracy, plus_accuracy, assertion_accuracy = test_function(task, generated_code)
    print(f"Final base input accuracy: {base_accuracy * 100:.2f}%")
    print(f"Final plus input accuracy: {plus_accuracy * 100:.2f}%")
    print(f"Final assertion accuracy: {assertion_accuracy * 100:.2f}%")
