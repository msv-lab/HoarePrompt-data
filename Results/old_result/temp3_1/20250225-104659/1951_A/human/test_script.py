# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call, import it
from program import func

# Otherwise, use the run_program_with_captured_io(input_data) function to run the program and capture the output
import io
import sys

def run_program_with_captured_io(input_data):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        with open("program.py", "r", encoding="utf-8") as f:
            code = f.read()
            exec(code, {})

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Write your test cases below
# Each test case should include assertions based on the problem description
# Example:
# assert function_name(input) == expected_output

# or if the program is a script we must execute 
# input_data = "input data"
# expected_output = "expected output"
# assert run_program_with_captured_io(input_data) == expected_output 

# Test cases for the provided program
input_data_1 = "3\n4\n1100\n3\n101\n2\n00"
expected_output_1 = "yes\nno\nyes"
assert run_program_with_captured_io(input_data_1) == expected_output_1

input_data_2 = "2\n1\n1\n2\n11"
expected_output_2 = "no\nno"
assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = "4\n5\n10101\n6\n111111\n7\n0000000\n8\n1001001"
expected_output_3 = "yes\nno\nyes\nno"
assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = "1\n0\n"
expected_output_4 = "yes"
assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = "1\n2\n10"
expected_output_5 = "yes"
assert run_program_with_captured_io(input_data_5) == expected_output_5

# End of script