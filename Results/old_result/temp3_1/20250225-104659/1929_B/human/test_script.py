# Import the function from the provided program
from program import func

# Define a helper function to capture the output of the function
import io
import sys

def capture_output(func, input_data):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        func()

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Write test cases below
# Each test case should include assertions based on the problem description

# Test case 1
input_data_1 = "7\n3 4\n3 3\n3 10\n3 9\n4 7\n7 11\n2 3"
expected_output_1 = "2\n2\n6\n5\n4\n6\n2"
assert capture_output(func, input_data_1) == expected_output_1

# Test case 2: Only one test case
input_data_2 = "1\n3 4"
expected_output_2 = "2"
assert capture_output(func, input_data_2) == expected_output_2

# Test case 3: All diagonals need to be colored
input_data_3 = "1\n3 10"
expected_output_3 = "6"
assert capture_output(func, input_data_3) == expected_output_3

# Test case 4: Minimum diagonals
input_data_4 = "1\n3 1"
expected_output_4 = "1"
assert capture_output(func, input_data_4) == expected_output_4

# Test case 5: Maximum diagonals
input_data_5 = "1\n3 14"
expected_output_5 = "7"
assert capture_output(func, input_data_5) == expected_output_5

# Test case 6: Large n and k
input_data_6 = "1\n100000000 400000000"
expected_output_6 = "200000000"
assert capture_output(func, input_data_6) == expected_output_6

# Test case 7: Edge case with small n and large k
input_data_7 = "1\n2 3"
expected_output_7 = "2"
assert capture_output(func, input_data_7) == expected_output_7

# Test case 8: Another edge case
input_data_8 = "1\n2 2"
expected_output_8 = "1"
assert capture_output(func, input_data_8) == expected_output_8

# Test case 9: Another edge case
input_data_9 = "1\n2 1"
expected_output_9 = "1"
assert capture_output(func, input_data_9) == expected_output_9

# Test case 10: Multiple test cases with different values
input_data_10 = "5\n3 4\n4 7\n5 14\n6 21\n7 28"
expected_output_10 = "2\n4\n7\n10\n14"
assert capture_output(func, input_data_10) == expected_output_10

# End of script