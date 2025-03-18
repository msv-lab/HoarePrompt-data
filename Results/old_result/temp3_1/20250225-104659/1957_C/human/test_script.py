# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import func_1, helper

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

# Test case 1 from the example
input_data = """3
4 1
1 2
8 1
7 6
1000 4
4 4
952 343
222 333
90 91"""
expected_output = """3
331
671968183"""
assert run_program_with_captured_io(input_data) == expected_output

# Additional test cases
# Test case 2: No initial moves
input_data = """1
4 0"""
expected_output = """72"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: Full board filled initially
input_data = """1
4 4
1 2
2 1
3 4
4 3"""
expected_output = """1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: Diagonal moves only
input_data = """1
4 2
1 1
2 2"""
expected_output = """9"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Large board with no initial moves
input_data = """1
1000 0"""
expected_output = str(helper(1000) % (10**9 + 7))
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Large board with some initial moves
input_data = """1
1000 5
1 2
2 1
3 4
4 3
5 5"""
expected_output = str(helper(995) % (10**9 + 7))
assert run_program_with_captured_io(input_data) == expected_output

# End of script