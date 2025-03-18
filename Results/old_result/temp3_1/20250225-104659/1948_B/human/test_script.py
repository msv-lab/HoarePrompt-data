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
    (
        "3\n4\n12 3 45 67\n3\n12 28 5\n2\n0 0",
        "YES\nNO\nYES"
    ),
    (
        "1\n5\n1 2 3 4 5",
        "YES"
    ),
    (
        "1\n5\n5 4 3 2 1",
        "NO"
    ),
    (
        "1\n3\n10 10 10",
        "YES"
    ),
    (
        "1\n3\n10 9 10",
        "NO"
    ),
    (
        "1\n4\n12 3 21 4",
        "NO"
    ),
    (
        "1\n4\n12 3 31 4",
        "YES"
    ),
    (
        "1\n2\n99 0",
        "YES"
    ),
    (
        "1\n2\n0 99",
        "YES"
    ),
    (
        "1\n2\n99 99",
        "YES"
    ),
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")