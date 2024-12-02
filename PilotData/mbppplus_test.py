import copy
import math
import re
import signal
import time
import json
from collections import Counter
from contextlib import contextmanager
from typing import Union, List, Tuple

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


def deep_compare(list1, list2):
    if len(list1) != len(list2):
        return False
    for elem in list1:
        if isinstance(elem, list):
            matched = False
            for candidate in list2:
                if isinstance(candidate, list) and deep_compare(elem, candidate):
                    matched = True
                    list2.remove(candidate)
                    break
            if not matched:
                return False
        else:
            if elem in list2:
                list2.remove(elem)
            else:
                return False

    return True


def round_elements(data: List, atol: float) -> List:
    if isinstance(data, list):
        return [round_elements(x, atol) if isinstance(x, (list, tuple)) else round(x / atol) * atol if isinstance(x, (int, float)) else x for x in data]
    return data


def convert_tuples_to_lists(obj):
    if isinstance(obj, tuple):
        return [convert_tuples_to_lists(item) for item in obj]
    elif isinstance(obj, list):
        return [convert_tuples_to_lists(item) for item in obj]
    else:
        return obj


def safe_compare(output, expected_output, flag, atol):
    try:
        # round
        if atol != 0:
            output = round_elements(output, atol)
            expected_output = round_elements(expected_output, atol)
        # tuple to list
        output = convert_tuples_to_lists(output)
        expected_output = convert_tuples_to_lists(expected_output)
        # if it should ignore order
        if flag:
            output_com = copy.deepcopy(output)
            expected_output_com = copy.deepcopy(expected_output)
            return deep_compare(output_com, expected_output_com)
        # if it shouldn't ignore order
        return output == expected_output
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


def remove_assert_statements(code_str):
    # 正则表达式匹配 assert 语句
    assert_pattern = r'^\s*assert.*(?:\r\n|\n|\r)?'
    # 删除所有 assert 语句
    cleaned_code = re.sub(assert_pattern, '', code_str, flags=re.MULTILINE)
    return cleaned_code

# Main function to test the generated code against the provided test cases
def test_function(task, generated_code):
    base_input = task['base_input']
    plus_input = task['plus_input']
    entry_point = task['entry_point']
    flag = task['order_ignored']
    reference_code = task['canonical_solution']
    assertion_tests = task.get('assertion', '')
    atol = task.get('atol', 0) # Absolute tolerance for floating point comparison
    generated_code = remove_assert_statements(generated_code)

    base_correct = 0  # Count of correct base input results
    failure_example = None # Store the first failure case which essentially are counterexamples

    # Base input testing with debug output
    for i, inputs in enumerate(base_input):
        test = copy.deepcopy(inputs)
        output_test = copy.deepcopy(inputs)
        base_ref_output, base_ref_error = execute_code(reference_code, entry_point, inputs)
        base_output, base_error = execute_code(generated_code, entry_point, test)
        if not base_ref_error and not base_error and safe_compare(base_output, base_ref_output, flag, atol=atol):
            base_correct += 1
            print(f"Base test {i + 1} passed.")
        elif base_ref_error and base_error:
            base_correct += 1
            print(f"Base test {i + 1} passed.")
        else:
            if base_error:
                print(f"Base test {i + 1} failed: {base_error}")
            elif base_ref_error:
                print(f"Base_ref test {i + 1} failed: {base_ref_error}")
            else:
                print(f"Base test {i + 1} failed: expected {base_ref_output}, got {base_output}")
            if failure_example is None:
                failure_example = {"test_type": "base", "input": output_test, "expected": base_ref_output,
                                   "got": base_output}

    base_accuracy = base_correct / len(base_input) if base_input else 0

    plus_correct = 0

    # Plus input testing with debug output
    for i, inputs in enumerate(plus_input):
        # preventing the process from being killed
        time.sleep(0.1)
        test = copy.deepcopy(inputs)
        output_test = copy.deepcopy(inputs)
        plus_ref_output, plus_ref_error = execute_code(reference_code, entry_point, inputs)
        plus_output, plus_error = execute_code(generated_code, entry_point, test)

        if not plus_ref_error and not plus_error and safe_compare(plus_output, plus_ref_output, flag, atol=atol):
            plus_correct += 1
            print(f"Plus test {i + 1} passed.")
        elif plus_ref_error and plus_error:
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
                failure_example = {"test_type": "plus", "input": output_test, "expected": plus_ref_output,
                                   "got": plus_output}

    plus_accuracy = plus_correct / len(plus_input) if plus_input else 0

    assertion_passed = False

    # Assertion tests with debug output
    if assertion_tests:
        assertion_code = f"""
{generated_code}

{assertion_tests}
        """ # Combine generated code with assertion tests
        print(assertion_code)
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
    task = {"task_id": "Mbpp/415", "prompt": "\"\"\"\nWrite a python function to find a pair with highest product from a given array of integers.\nassert max_Product([1,2,3,4,7,0,8,4]) == (7,8)\n\"\"\"\n", "entry_point": "max_Product", "canonical_solution": "\ndef max_Product(arr): \n    pairs = [(a, b) for a in arr for b in arr if a != b]\n    return max(pairs, key=lambda x: x[0] * x[1])\n", "base_input": [[[1, 2, 3, 4, 7, 0, 8, 4]], [[0, -1, -2, -4, 5, 0, -6]], [[1, 2, 3]]], "atol": 0, "plus_input": [[[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[10, -20, 30, -40, 50, -60, 70, -80, 90, -100]], [[2, 3, 5, 7, 11, 13, 17]], [[-5, -10, -20, -30, -1, 0, 1, 2, 3, 4, 5, 10, 20, 30]], [[1000000, 2000000, 3000000, 4000000]], [[999999, 1000000, 1000001]], [[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]], [[999999999, 888888888, -777777777, 666666666, -555555555]], [[1000, -2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000, -10000]], [[-10000, 20000, -30000, 40000, -50000, 60000, -70000, 80000, -90000, 100000]], [[1000000, -1000000, 999999, -999999, 888888, -888888, 777777, -777777]], [[1000000000, 2000000000, 3000000000, 4000000000, 5000000000]], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]], [[100, 200, 300, 401, 500, 600, 700, 800, 1000]], [[-2, -1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 10]], [[-2, -1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 9]], [[2, 16, 3, 5, 12, 13, 17, 7]], [[1000000, 2000000, 3000000, 4000000, 4000000]], [[-5, -10, -20, -30, -1, 0, 1, 2, 3, 4, 5, 10, 20, 30, 2]], [[-10000, 20000, -30000, 40000, -50000, -70000, 60000, 80000, -90000, 100000]], [[-1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 8]], [[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[-2, -1, 0, 1, 2, 3, 4, 5, -555555555, 7, 8, 9, 10]], [[-1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 8, 6]], [[1000000, 2000000, 3000000, 4000000, 1000000]], [[100, 200, 201, 300, 400, 500, 600, 700, 800, 900, 1000, 1000]], [[1000000, 3000000, 4000000, 4000000]], [[100, 200, 301, 400, 500, 600, 700, 800, 900, 1000]], [[-1, 0, 1, 2, 800, 5, 6, -50000, 7, 8, 9, 8, 6]], [[-1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 8, 6, 1]], [[-1000000, 999999, -999999, 888888, -888888, 777777, -777777]], [[100, 20, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900]], [[1000000, 2000000, 4000000, 1000000]], [[-2, -1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 10, 7]], [[10, -20, 30, -40, 50, 11, 10, -60, 70, -80, 90, -100, 10]], [[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2, 300, 800]], [[100, 200, -888888, 401, 500, 600, 700, 800, 1000]], [[-2, -1, 0, 1, 2, 4, 3, 4, 5, -555555555, 7, 8, 9, 10]], [[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 6]], [[999999999, 888888888, -777777777, -555555555]], [[-2, -1, 1000000000, 1, 2, 800, 70, 6, 7, 8, 9, 9]], [[-1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 8, 6, 0]], [[200, 201, 300, 400, 500, 600, 700, 900, 1000, 1000]], [[2, 4, 6, 8, 10, 13, 14, 16, 18, 20]], [[2, 17, 3, 5, 12, 13, 17, 7]], [[-2, -1, 0, 1, 2, 800, 5, 6, 7, 8, 9, 10, 7, 9]], [[100, 200, 300, 400, 500, 601, 700, 800, 5000, -6000]], [[100, 200, 300, 400, 300, 500, 700, 800, 900, 1000, 200]], [[-1, 0, 1, 2, 800, 4, 5, 6, 7, 8, 9, 8, 6, 1]], [[-1, 0, 1, 1, 800, 5, 6, 7, 8, 9, 8, 6, -1]], [[10, -20, 30, -40, 50, -60, 70, -80, -100]], [[-2, -1, 0, 1, 2, 3, 4, 5, -555555555, 7, 8, 9, 10, 8]], [[-1, 0, 1, 0, 2, 800, 5, 6, 7, 8, 601, 9, 8]], [[-2, -1, 0, 1, 2, 801, 5, 6, 7, 8, 9, 10, 7]], [[-2, -1, 0, 1, 2, 800, 5, 7, 8, 9, -90000, 7, 7]], [[10, -20, 30, -40, 50, -60, 70, -80, -100, 10]], [[100, 200, 201, 300, 400, 500, 600, 700, 800, 900, 1000, -6000, 1000]], [[-10000, 20000, -30000, 1000001, 40000, -50000, 60000, -70000, 80000, -90000, 100000]], [[1000000, 2000000, 100, 4000000, 4000000]], [[-2, -1, 0, 1, 2, 3, 5000000000, 5, 6, 7, 8, 9, 6]], [[-1000000, 999999, -999999, 888888, -888888, 777777, -777777, -999999]], [[-10000, 20000, -30000, 40000, -50000, 60000, -70000, 80000, -90000, 100000, -90000]], [[20000, -30000, 1000001, 40000, 888888888, -50000, 60000, 80000, -90000, 100000]], [[100, 200, 4999, 300, 400, 601, 700, 800, 5000, -6000]], [[100, 200, 300, 400, 500, 600, 700, 900, 1000]], [[100, -888888, 401, 500, 600, 700, 800, 1000]], [[-2, -1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 6, 6]], [[100, 200, 300, 400, 500, 601, 700, 800, 5000, -6000, 500]], [[100, 200, 201, 300, 400, 500, 600, -5, 700, 800, 900, 1000, -6000, 1000, 600]], [[-2, -1, 0, 1, 2, -40, 5, 6, 7, 8, 9, 10, 7]], [[2, 4, 6, 301, 8, 10, 13, 14, 16, 18, 20]], [[-1, 0, 1, 2, 800, 5, 6, -50000, 7, 8, 9, 8]], [[1000000, -1000000, 999999, -999999, 888888, -888888, 777777, -777777, 999999]], [[1000000, 4000000, 2000000, 4000000]], [[20000, -30000, 1000001, 666666666, 40000, 888888888, -50000, 60000, 80000, -90000, 100000]], [[100, 200, 300, 400, 300, 500, 700, 3000000, 800, 900, 1000, 200]], [[-1, 0, 1, 2, 800, 5, 6, -50000, 7, 8, 9, 8, 6, -1]], [[20000, -30000, 666666666, 40000, 888888888, -50000, 60000, 80000, -90000, 100000, 60000]], [[-1, 0, 1, 2, 800, 5, 6, -50000, 7, 8, 9, 8, 6, 5]], [[-1, 0, 1, 0, 2, 800, 5, 6, 7, 8, 601, 9, 8, 0, 2]], [[100, 200, 201, 300, 400, 500, 600, -5, 700, 800, 1000, -6000, 1000, 600]], [[100, 199, 300, 400, 500, 601, 700, 800, 5000, -6000, 601]], [[-1, 0, 1, 2, -40, 5, 6, 7, 8, 9, 10, 7]], [[-1, 0, 1, 3, 2, 800, 5, 6, -50000, 7, 8, 9, 9]], [[-2, -1, -1, 1, 2, 4, 3, 4, 5, -555555555, 7, 8, 9, 10]], [[100, 199, 300, 400, 500, 601, 700, 800, 5000, -6000, 601, 800]], [[100, 200, 300, 400, 101, 500, 600, 700, 900, 1000, 200, 200]], [[1000000, -1000000, 1000000, -999999, 888888, -888888, 777777, -777777, 999999]], [[999999, 1000000, -999999, 888888, 777777, -777777, 999999, 999999]], [[100, 200, 201, 300, 400, 500, 600, -5, 700, 9000, 900, 1000, -6000, 1000, 600]], [[100, 199, 300, 400, 601, 700, 800, 5000, -6000, 601, 800, 700]], [[100, 200, 201, 300, 400, 500, 600, 700, 14, 800, 900, 1000, -6000, 1000]], [[200, 201, 300, 400, 500, 600, 700, 900, 1000, 1000, 600]], [[100, 199, 300, 400, 500, 601, 101, 700, 800, 5000, -6000, 601]], [[-20, 30, -40, 50, -60, 900, 70, -80, 90, -100]], [[-1, 0, 1, 2, 800, 5, 6, -50000, 7, 8, 9, 8, 6, 6]], [[-2, -1, 0, 1, 2, 4, 5, 5, 7, 8, 9, 0]], [[-1, 0, 1, 3, 2, 2000000000, 800, 5, 6, -50000, 7, 8, 9, 9]], [[100, 200, 400, 101, 500, 600, 700, 900, 1000, 200, 200]], [[-1, 0, 1, 0, 2, 800, 5, 6, 8, 8, 601, 9, 8, 0, 2]], [[-20, 30, -40, 50, -79, -60, 900, 70, -80, 90]], [[20000, -30000, 1000001, 39999, 888888888, -50000, 60000, -79, -90000, 100000]], [[-2, -1, 0, 1, 2, 3, 4, 6, 7, 8, 9]], [[-20, 30, -40, 50, -60, 900, 70, 90, -100, -20]], [[100, 200, -888888, 401, 500, 700, 800, 1000]], [[-1000000, 999999, -999999, 888888, 199, 777777, -777777]], [[-1, 0, 2, -40, 5, 6, 7, 8, 9, 10, 7]], [[-2, -1, 0, 1, 2, 5, 5, 5, 7, 8, 9, 0]], [[-2, -1, -1, 1, 2, 4, 3, 4, -555555555, 7, 8, 9, 10]], [[-2, -1, 0, 1, 2, -1000000, 4, 6, 7, 8, 9, 7]], [[1000000, 30, 4000000, 1000000]], [[-1, 0, 1, 2, 800, -5, 5, 7, 8, 1, 9, 8, 6, 1]], [[-2, -1, 0, 1, 2, 800, 5, 6, 8, 9, 9]]], "contract": "\n    assert isinstance(arr, list), \"invalid inputs\" # $_CONTRACT_$\n    assert len(arr) >= 2, \"invalid inputs\" # $_CONTRACT_$\n    assert all(isinstance(i, int) for i in arr), \"invalid inputs\" # $_CONTRACT_$\n", "assertion": "\nassert max_Product([1,2,3,4,7,0,8,4]) == (7,8)\nassert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)\nassert max_Product([1,2,3]) == (2,3)\n", "order_ignored":False}
    generated_code = """
def max_Product(arr):\n    if len(arr) < 2:\n        raise ValueError(\"Array must have at least two integers\")\n    \n    arr.sort()\n    \n    # Product of the two largest numbers\n    max1 = arr[-1]\n    max2 = arr[-2]\n    \n    # Product of the two smallest numbers (in case of negative numbers)\n    min1 = arr[0]\n    min2 = arr[1]\n    \n    if max1 * max2 > min1 * min2:\n        return (max2, max1)\n    else:\n        return (min1, min2)\n\n# Tests\nassert max_Product([1,2,3,4,7,0,8,4]) == (7,8)\nassert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)\nassert max_Product([1,2,3]) == (2,3)\n
    """

    base_accuracy, plus_accuracy, assertion_passed, failure_example = test_function(task, generated_code)
    print(f"\nFinal base input accuracy: {base_accuracy}")
    print(f"Final plus input accuracy: {plus_accuracy}")
    print(f"Final assertion passed: {assertion_passed}")
    print(f"Failure example: {failure_example}")
