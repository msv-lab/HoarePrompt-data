# Import the function from the provided program
from program import func

# Helper function to automate input/output capture and execute `program.py` safely
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

# Test cases
# Test case 1: Example from the problem statement
input_data = """3\n4\n0 0 1 1\n4\n0 1 2 3\n2\n1 1"""
expected_output = "2\n1\n0"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2: All zeros
input_data = """1\n5\n0 0 0 0 0"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: All distinct elements
input_data = """1\n5\n0 1 2 3 4"""
expected_output = "5"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: Single element
input_data = """1\n1\n0"""
expected_output = "1"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: No zeros
input_data = """1\n5\n1 2 3 4 5"""
expected_output = "0"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Multiple test cases with different scenarios
input_data = """4\n3\n0 0 0\n3\n1 1 1\n3\n0 1 2\n3\n0 1 1"""
expected_output = "1\n0\n3\n2"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7: Large input with many zeros
input_data = """1\n100000\n" + "0 "*99999 + "1"""
expected_output = "2"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 8: Large input with no zeros
input_data = """1\n100000\n" + " ".join(map(str, range(1, 100001)))"""
expected_output = "0"
assert run_program_with_captured_io(input_data) == expected_output

# End of script