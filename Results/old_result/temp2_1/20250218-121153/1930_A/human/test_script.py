# Include necessary imports if any
import io
import sys

# Assuming the provided program is saved as 'program.py' and can be imported from the same directory.
from program import func

# Helper function to automate input/output capture
def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test Case 1: Single move
input_data = "1\n1\n2 3"
expected_output = "2"
assert capture_output(func, input_data) == expected_output

# Test Case 2: Two moves
input_data = "1\n2\n1 1 2 1"
expected_output = "2"
assert capture_output(func, input_data) == expected_output

# Test Case 3: Three moves
input_data = "1\n3\n1 1 1 1 1 1"
expected_output = "3"
assert capture_output(func, input_data) == expected_output

# Test Case 4: Multiple test cases
input_data = "3\n1\n2 3\n2\n1 1 2 1\n3\n1 1 1 1 1 1"
expected_output = "2\n2\n3"
assert capture_output(func, input_data) == expected_output

# Test Case 5: Larger input values
input_data = "1\n50\n10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000"
expected_output = "250000000"
assert capture_output(func, input_data) == expected_output

# Test Case 6: Minimum value inputs
input_data = "1\n50\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
expected_output = "50"
assert capture_output(func, input_data) == expected_output

# Test Case 7: Mixed values
input_data = "1\n5\n1 10 2 20 3 30 4 40 5 50"
expected_output = "15"
assert capture_output(func, input_data) == expected_output

# End of script