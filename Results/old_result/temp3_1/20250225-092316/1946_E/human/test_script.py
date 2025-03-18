# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import func_2

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

# Test case 1
input_data = """1
1 1 1
1
1"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2
input_data = """1
4 2 3
1 2
2 3 4"""
expected_output = "3"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3
input_data = """1
3 3 1
1 2 3
3"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4
input_data = """1
5 3 4
1 2 3
2 3 4 5"""
expected_output = "0"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5
input_data = """1
20 5 4
1 2 3 4 12
12 13 18 20"""
expected_output = "317580808"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6
input_data = """1
6 2 3
1 3
3 4 6"""
expected_output = "10"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7
input_data = """2
1 1 1
1
1
4 2 3
1 2
2 3 4"""
expected_output = "1\n3"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 8: Edge case with small n
input_data = """1
2 1 1
1
2"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 9: Edge case with large n
input_data = """1
200000 1 1
1
200000"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 10: Multiple test cases with different scenarios
input_data = """5
1 1 1
1
1
4 2 3
1 2
2 3 4
3 3 1
1 2 3
3
5 3 4
1 2 3
2 3 4 5
6 2 3
1 3
3 4 6"""
expected_output = "1\n3\n1\n0\n317580808\n10"
assert run_program_with_captured_io(input_data) == expected_output

# End of script