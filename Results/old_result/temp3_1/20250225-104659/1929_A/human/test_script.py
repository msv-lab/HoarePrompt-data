# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import func

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
# Example:
# assert function_name(input) == expected_output

# or if the program is a script we must execute 
input_data = """5
3
2 1 3
3
69 69 69
5
100 54 80 43 90
4
3 4 3 3
2
2 1"""
expected_output = """2
0
57
1
1"""
assert run_program_with_captured_io(input_data) == expected_output

# Additional test cases
input_data = """2
4
1 2 3 4
4
4 3 2 1"""
expected_output = """3
3"""
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
2
1000000000 1"""
expected_output = """999999999"""
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
3
1 1 1"""
expected_output = """0"""
assert run_program_with_captured_io(input_data) == expected_output

input_data = """1
10
1 2 3 4 5 6 7 8 9 10"""
expected_output = """9"""
assert run_program_with_captured_io(input_data) == expected_output

# End of script