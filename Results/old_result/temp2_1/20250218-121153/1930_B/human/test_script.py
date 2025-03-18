import io
import sys

from program import func

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Test cases
test_cases = [
    ("2\n4\n3", "4 1 2 3\n1 2 3"),
    ("1\n5", "5 1 4 2 3"),
    ("1\n6", "6 1 5 2 4 3"),
    ("1\n7", "7 1 6 2 5 3 4"),
    ("1\n8", "8 1 7 2 6 3 5 4"),
    ("1\n9", "9 1 8 2 7 3 6 4 5"),
    ("1\n10", "10 1 9 2 8 3 7 4 6 5")
]

# Running test cases
for input_data, expected_output in test_cases:
    actual_output = capture_output(func, input_data)
    assert actual_output == expected_output, f"Failed for input: {input_data}\nExpected: {expected_output}\nGot: {actual_output}"

print("All test cases passed.")