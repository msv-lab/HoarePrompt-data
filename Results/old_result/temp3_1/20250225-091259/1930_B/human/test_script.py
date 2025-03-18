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

# Test case 1: Given in the problem statement
input_data = "2\n4\n3"
expected_output = "4 1 2 3\n1 2 3"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2: Small input
input_data = "1\n3"
expected_output = "1 2 3"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: Larger input
input_data = "1\n10"
expected_output = "1 10 2 9 3 8 4 7 5 6"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: Multiple test cases with varying n
input_data = "3\n5\n6\n7"
expected_output = "1 5 2 4 3\n1 6 2 5 3 4\n1 7 2 6 3 5 4"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Edge case where n is the maximum allowed value
input_data = "1\n100000"
expected_output = " ".join(str(i) if i % 2 == 0 else str(100001 - i) for i in range(1, 100001))
assert run_program_with_captured_io(input_data) == expected_output

# End of script