# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import *

# otherwise use the run_program_with_captured_io(input_data) function to run the program and capture the output
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
input_data = """7
5
1 3 5 5 2
5
2 4 4 5 1
5
0 1 3 3 1
6
5 6 0 2 3 0
4
1 2 7 2
3
7 1 0
4
1 1 1 1"""
expected_output = "YES\nNO\nYES\nNO\nNO\nNO\nNO"
assert run_program_with_captured_io(input_data) == expected_output

# Additional test cases
input_data = """1
3
1 2 1"""
expected_output = "YES"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
3
0 0 0"""
expected_output = "YES"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
4
1 0 1 0"""
expected_output = "NO"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
5
1 1 1 1 1"""
expected_output = "NO"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
5
0 1 2 1 0"""
expected_output = "YES"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
5
2 2 2 2 2"""
expected_output = "YES"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
5
3 3 3 3 3"""
expected_output = "YES"
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
5
1 3 3 3 1"""
expected_output = "YES"
assert run_program_with_captured_io(input_data) == expected_output

# End of script