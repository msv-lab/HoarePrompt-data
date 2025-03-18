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
    ("3\n7 3\n6 4\n255 8", "YES\n10\n2 3 4 5 6 7 8 9 10 11\nNO\nYES\n8\n128 64 32 16 8 4 2 1"),
    ("1\n1 1", "YES\n1\n1"),
    ("1\n10 1", "YES\n1\n1"),
    ("1\n10 10", "YES\n1\n1"),
    ("1\n10 2", "YES\n2\n5 1"),
    ("1\n100 50", "YES\n2\n50 1"),
    ("1\n100 99", "YES\n2\n99 1"),
    ("1\n100 98", "NO"),
    ("1\n1000000000000000000 1", "YES\n1\n1"),
    ("1\n1000000000000000000 1000000000000000000", "YES\n1\n1"),
    ("1\n1000000000000000000 999999999999999999", "YES\n2\n999999999999999999 1"),
]

# Run the test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")