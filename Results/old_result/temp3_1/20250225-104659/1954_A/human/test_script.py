import io
import sys
from program import func

def run_program_with_captured_io(input_data):
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
input_data_1 = "5\n1 1 1\n5 1 1\n5 2 1\n5 2 2\n5 5 3"
expected_output_1 = "NO\nNO\nYES\nNO\nYES"

input_data_2 = "3\n2 2 1\n3 3 2\n4 4 3"
expected_output_2 = "YES\nNO\nNO"

input_data_3 = "1\n50 50 49"
expected_output_3 = "YES"

input_data_4 = "2\n10 1 1\n10 10 9"
expected_output_4 = "NO\nYES"

input_data_5 = "1\n3 2 2"
expected_output_5 = "NO"

# Running assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

print("All test cases passed!")