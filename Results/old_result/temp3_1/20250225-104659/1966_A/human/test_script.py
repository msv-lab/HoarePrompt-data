# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import *

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

# Test case 1: Example from the problem statement
input_data = """7
5 3
4 1 1 4 4
1 10
7
7 2
4 2 1 100 5 2 3
10 4
1 1 1 1 1 1 1 1 1 1
5 2
3 8 1 48 7
6 2
10 20 30 10 20 40
6 3
10 20 30 10 20 40"""
expected_output = """2
1
1
3
5
1
6"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2: Single card with k > 1
input_data = """1
1 3
1"""
expected_output = """1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: All cards are the same
input_data = """1
6 3
1 1 1 1 1 1"""
expected_output = """2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: No operations can be performed
input_data = """1
3 4
1 2 3"""
expected_output = """3"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Multiple test cases with different k values
input_data = """3
4 2
1 1 2 2
4 3
1 1 1 1
4 4
1 1 1 1"""
expected_output = """2
1
1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Large n with all cards different
input_data = """1
100 2
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100"""
expected_output = """100"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7: Large n with some cards the same
input_data = """1
100 2
1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20 20 21 21 22 22 23 23 24 24 25 25 26 26 27 27 28 28 29 29 30 30 31 31 32 32 33 33 34 34 35 35 36 36 37 37 38 38 39 39 40 40 41 41 42 42 43 43 44 44 45 45 46 46 47 47 48 48 49 49 50 50"""
expected_output = """50"""
assert run_program_with_captured_io(input_data) == expected_output

# End of script