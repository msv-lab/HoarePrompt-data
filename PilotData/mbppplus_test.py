import math
import signal
import time
import json
from contextlib import contextmanager

TIME_LIMIT = 3

# Exception to handle timeout errors
class TimeoutException(Exception):
    pass

# Handler function that raises a TimeoutException when the execution time exceeds the limit
def timeout_handler(signum, frame):
    raise TimeoutException("Execution timed out")

# Context manager to enforce a time limit on a block of code
@contextmanager
def time_limit(seconds):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        yield
    except TimeoutException as e:
        raise TimeoutException("Execution exceeded time limit")
    finally:
        signal.alarm(0)

# Function to execute the generated Python code within a time limit
def execute_code(code_str: str, entry_point: str, inputs):
    try:
        with time_limit(TIME_LIMIT):
            exec_globals = {} # Dictionary to hold the global variables created by exec
            exec(code_str, exec_globals)
            fn = exec_globals[entry_point]
            result = fn(*inputs)
            return result, None
    except TimeoutException as te:
        return None, "TimeoutError: Execution exceeded time limit" # Handle timeout error
    except Exception as e:
        return None, str(e)  # Handle any other exception and return the error message

# Safely compare the output to the expected output, handling floating point numbers
def safe_compare(output, expected_output, atol):
    try:
        if atol == 0:
            return output == expected_output
        return math.isclose(output, expected_output, abs_tol=atol)
    except Exception as e:
        print(f"Comparison error: {e}")
        return False

# Attempt to serialize an object; if non-serializable, return a string representation
def safe_serialize(obj):
    try:
        json.dumps(obj)
        return obj
    except (TypeError, OverflowError):
        return f"(non-serializable) {str(obj)}"

# Main function to test the generated code against the provided test cases
def test_function(task, generated_code):
    base_input = task['base_input']
    plus_input = task['plus_input']
    entry_point = task['entry_point']
    reference_code = task['canonical_solution']
    assertion_tests = task.get('assertion', '')
    atol = task.get('atol', 0) # Absolute tolerance for floating point comparison

    base_correct = 0  # Count of correct base input results
    failure_example = None # Store the first failure case which essentially are counterexamples

    # Base input testing with debug output
    for i, inputs in enumerate(base_input):

        base_ref_output, base_ref_error = execute_code(reference_code, entry_point, inputs)
        base_output, base_error = execute_code(generated_code, entry_point, inputs)

        if not base_ref_error and not base_error and safe_compare(base_output, base_ref_output, atol=atol):
            base_correct += 1
            print(f"Base test {i + 1} passed.")
        else:
            if base_error:
                print(f"Base test {i + 1} failed: {base_error}")
            elif base_ref_error:
                print(f"Base test {i + 1} failed: {base_ref_error}")
            else:
                print(f"Base test {i + 1} failed: expected {base_ref_output}, got {base_output}")
            if failure_example is None:
                failure_example = {"test_type": "base", "input": inputs, "expected": base_ref_output,
                                   "got": base_output}

    base_accuracy = base_correct / len(base_input) if base_input else 0

    plus_correct = 0

    # Plus input testing with debug output
    for i, inputs in enumerate(plus_input):
        # preventing the process from being killed
        time.sleep(0.1)
        plus_ref_output, plus_ref_error = execute_code(reference_code, entry_point, inputs)
        plus_output, plus_error = execute_code(generated_code, entry_point, inputs)

        if not plus_ref_error and not plus_error and safe_compare(plus_output, plus_ref_output, atol=atol):
            plus_correct += 1
            print(f"Plus test {i + 1} passed.")
        else:
            if plus_error:
                print(f"Plus test {i + 1} failed: {plus_error}")
            elif plus_ref_error:
                print(f"Plus test {i + 1} failed: {plus_ref_error}")
            else:
                print(f"Plus test {i + 1} failed: expected {plus_ref_output}, got {plus_output}")
            if failure_example is None:
                failure_example = {"test_type": "plus", "input": inputs, "expected": plus_ref_output,
                                   "got": plus_output}

    plus_accuracy = plus_correct / len(plus_input) if plus_input else 0

    assertion_passed = False

    # Assertion tests with debug output
    if assertion_tests:
        assertion_code = f"""
{generated_code}

{assertion_tests}
        """ # Combine generated code with assertion tests
        try:
            with time_limit(TIME_LIMIT):
                exec_globals = {}
                exec(assertion_code, exec_globals)
                assertion_passed = True
                print("All assertion tests passed.")
        except TimeoutException as te:
            print(f"Assertion tests failed: {te}")
            if failure_example is None:
                failure_example = {"test_type": "assertion",
                                   "error": "TimeoutError: Assertion execution exceeded time limit"}
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            if failure_example is None:
                failure_example = {"test_type": "assertion", "error": str(e)}
        except Exception as e:
            print(f"Error during assertion tests: {e}")
            if failure_example is None:
                failure_example = {"test_type": "assertion", "error": str(e)}

    print(f"\nBase input accuracy: {base_accuracy * 100:.2f}%")
    print(f"Plus input accuracy: {plus_accuracy * 100:.2f}%")
    print(f"Assertion tests passed: {assertion_passed}")

    # if not serializable, change it to str. i.e. counterexample for task Mbpp/590 use complex object.
    failure_example = safe_serialize(failure_example)

    return base_accuracy, plus_accuracy, assertion_passed, failure_example


# example case
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
        "atol": 0,
        "assertion": "assert similar_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)\nassert similar_elements((1, 2, 3, 4), (5, 4, 3, 7)) == (3, 4)\n"
    }

    generated_code = """
def similar_elements(test_tup1, test_tup2):
    return tuple(set(test_tup1) & set(test_tup2))
"""

    base_accuracy, plus_accuracy, assertion_passed, failure_example = test_function(task, generated_code)
    print(f"\nFinal base input accuracy: {base_accuracy * 100:.2f}%")
    print(f"Final plus input accuracy: {plus_accuracy * 100:.2f}%")
    print(f"Final assertion passed: {assertion_passed}")
    print(f"Failure example: {failure_example}")
