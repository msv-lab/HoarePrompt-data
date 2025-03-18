# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import func_1

# Otherwise use the run_program_with_captured_io(input_data) function to run the program and capture the output
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

# Test cases for the function func_1
assert func_1(2, 0) == 2
assert func_1(2, 1) == 1
assert func_1(4, 1) == 4
assert func_1(5, 10) == 1
assert func_1(5, 3) == 5
assert func_1(4, 4) == 1

# Test cases for the entire script
input_data = """6\n2 0\n2 1\n4 1\n5 10\n5 3\n4 4"""
expected_output = "2\n1\n4\n1\n5\n1"
assert run_program_with_captured_io(input_data) == expected_output

# Additional edge cases
input_data = """1\n1 0"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1\n2 1"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1\n3 2"""
expected_output = "2"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1\n3 3"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# End of script