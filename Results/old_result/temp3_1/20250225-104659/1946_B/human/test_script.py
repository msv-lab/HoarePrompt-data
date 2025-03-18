# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

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

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test case 1
input_data = """1
2 2
-4 -7"""
expected_output = "999999996"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2
input_data = """1
3 3
2 2 8"""
expected_output = "96"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3
input_data = """1
1 7
7"""
expected_output = "896"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4
input_data = """1
5 1
4 -2 8 -12 9"""
expected_output = "17"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5
input_data = """1
7 4
8 14 -9 6 0 -1 3"""
expected_output = "351"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6
input_data = """1
7 100
5 3 -8 12 -5 -9 3"""
expected_output = "716455332"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7
input_data = """1
6 1000
-1000000000 -1000000000 -1000000000 -1000000000 -1000000000 -1000000000"""
expected_output = "42"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 8
input_data = """1
2 1
1000000000 8"""
expected_output = "2"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 9
input_data = """1
5 4
0 0 0 0 0"""
expected_output = "0"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 10
input_data = """1
6 10
48973 757292 58277 -38574 27475 999984"""
expected_output = "897909241"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 11
input_data = """1
7 1
-1000 1000 -1000 1000 -1000 1000 -1000"""
expected_output = "0"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 12
input_data = """1
10 10050
408293874 -3498597 7374783 295774930 -48574034 26623784 498754833 -294875830 283045804 85938045"""
expected_output = "416571966"
assert run_program_with_captured_io(input_data) == expected_output

# End of script