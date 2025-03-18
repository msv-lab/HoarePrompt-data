# Import the necessary function from the provided program
from program import func

# Helper function to capture output from the function
import io
import sys

def run_function_with_captured_io(func, input_data):
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

# Test cases
# Each test case should include assertions based on the problem description

# Test case 1
input_data_1 = "6\n11010\n00000000\n1\n10\n0001111\n0110"
expected_output_1 = "3\n1\n1\n2\n1\n2"
assert run_function_with_captured_io(func, input_data_1) == expected_output_1

# Test case 2: All zeros
input_data_2 = "1\n00000000"
expected_output_2 = "1"
assert run_function_with_captured_io(func, input_data_2) == expected_output_2

# Test case 3: All ones
input_data_3 = "1\n11111111"
expected_output_3 = "1"
assert run_function_with_captured_io(func, input_data_3) == expected_output_3

# Test case 4: Single character (zero)
input_data_4 = "1\n0"
expected_output_4 = "1"
assert run_function_with_captured_io(func, input_data_4) == expected_output_4

# Test case 5: Single character (one)
input_data_5 = "1\n1"
expected_output_5 = "1"
assert run_function_with_captured_io(func, input_data_5) == expected_output_5

# Test case 6: Alternating zeros and ones
input_data_6 = "1\n01010101"
expected_output_6 = "8"
assert run_function_with_captured_io(func, input_data_6) == expected_output_6

# Test case 7: Multiple test cases with different patterns
input_data_7 = "3\n111000\n001100\n101010"
expected_output_7 = "2\n3\n6"
assert run_function_with_captured_io(func, input_data_7) == expected_output_7

# Test case 8: Edge case with one transition
input_data_8 = "1\n10"
expected_output_8 = "2"
assert run_function_with_captured_io(func, input_data_8) == expected_output_8

# Test case 9: Edge case with no transitions
input_data_9 = "1\n00000000000000000000"
expected_output_9 = "1"
assert run_function_with_captured_io(func, input_data_9) == expected_output_9

# Test case 10: Edge case with multiple transitions
input_data_10 = "1\n10101010101010101010"
expected_output_10 = "20"
assert run_function_with_captured_io(func, input_data_10) == expected_output_10

# End of script