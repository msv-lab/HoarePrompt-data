# Import the helper function to capture input/output if needed
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

# Import the function from the provided program if it defines one
# In this case, the program defines a function named `func`
from program import func

# Test cases
test_cases = [
    ("1\n7 1\n", "1"),
    ("1\n7 2\n", "3"),
    ("1\n7 3\n", "5"),
    ("1\n7 4\n", "7"),
    ("1\n7 5\n", "2"),
    ("1\n7 6\n", "6"),
    ("1\n7 7\n", "4"),
    ("1\n1 1\n", "1"),
    ("1\n34 14\n", "27"),
    ("1\n84 19\n", "37"),
    ("1\n1000000000 1000000000\n", "536870912"),
]

# Run the test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")