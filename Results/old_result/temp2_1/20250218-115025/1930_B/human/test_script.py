# This script tests the correctness of the 'func' function from the provided 'program.py'.

import sys
from io import StringIO
from unittest.mock import patch
from program import func

# Function to capture output from the func
def capture_output(func, input_data):
    with patch('builtins.input', side_effect=input_data):
        # Redirect stdout to capture the function's printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        func()
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

# Test cases
test_cases = [
    {
        "input": ["2", "4", "3"],
        "expected": "4 1 2 3\n1 2 3"
    },
    {
        "input": ["1", "5"],
        "expected": "5 1 4 2 3"
    },
    {
        "input": ["1", "7"],
        "expected": "7 1 6 2 5 3 4"
    },
    {
        "input": ["3", "3", "4", "5"],
        "expected": "1 2 3\n4 1 2 3\n5 1 4 2 3"
    }
]

# Run test cases
for idx, test_case in enumerate(test_cases):
    input_data = test_case["input"]
    expected_output = test_case["expected"]
    actual_output = capture_output(func, input_data)
    assert actual_output == expected_output, f"Test case {idx + 1} failed: Expected {expected_output}, got {actual_output}"
    print(f"Test case {idx + 1} passed.")

print("All test cases passed.")