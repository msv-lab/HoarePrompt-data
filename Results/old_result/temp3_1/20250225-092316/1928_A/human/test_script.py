# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

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
test_cases = [
    ("1\n1 1", "No"),
    ("1\n2 1", "No"),
    ("1\n2 6", "Yes"),
    ("1\n3 2", "Yes"),
    ("1\n2 2", "Yes"),
    ("1\n2 4", "Yes"),
    ("1\n6 3", "No"),
    ("7\n1 1\n2 1\n2 6\n3 2\n2 2\n2 4\n6 3", "No\nNo\nYes\nYes\nYes\nYes\nNo"),
    ("1\n4 3", "Yes"),
    ("1\n5 5", "No"),
    ("1\n8 4", "Yes"),
    ("1\n10 2", "Yes"),
    ("1\n1 2", "No"),
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")