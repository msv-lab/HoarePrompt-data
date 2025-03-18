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
    ("1\n43\n", "YES"),
    ("2\n1 3\n", "NO"),
    ("5\n4 5 2 1 3\n", "YES"),
    ("3\n1 2 3\n", "NO"),
    ("7\n4 5 5 0 6 4 4\n", "NO"),
    ("7\n6 5 5 1 3 4 4\n", "YES"),
    ("1\n0\n", "YES"),
    ("2\n0 0\n", "YES"),
    ("3\n1 1 1\n", "YES"),
    ("4\n1 2 3 4\n", "NO"),
    ("5\n5 5 5 5 5\n", "YES"),
    ("6\n1 2 3 4 5 6\n", "NO"),
    ("10\n1 2 3 4 5 6 7 8 9 10\n", "NO"),
    ("10\n10 10 10 10 10 10 10 10 10 10\n", "YES"),
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")