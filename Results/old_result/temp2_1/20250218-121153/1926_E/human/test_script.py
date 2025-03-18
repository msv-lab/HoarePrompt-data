import io
import sys

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Assuming the provided program is saved as 'program.py' and can be imported from the same directory.
from program import func

# Test cases
test_cases = [
    ("11\n7 1\n7 2\n7 3\n7 4\n7 5\n7 6\n7 7\n1 1\n34 14\n84 19\n1000000000 1000000000", "1\n3\n5\n7\n2\n6\n4\n1\n27\n37\n536870912"),
    ("1\n10 5", "9"),
    ("1\n10 10", "8"),
    ("1\n100 1", "1"),
    ("1\n100 100", "64"),
    ("1\n5 5", "4"),
    ("1\n20 20", "16"),
    ("1\n50 50", "32"),
    ("1\n1000 1000", "512")
]

# Run test cases
for input_data, expected_output in test_cases:
    actual_output = capture_output(func, input_data)
    assert actual_output == expected_output, f"Test failed for input {input_data}. Expected {expected_output}, got {actual_output}"

print("All tests passed!")