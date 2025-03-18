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
        "5\n8\n0 1 1 1 0 1 1 0\n6\n0 1 0 0 0 0\n6\n1 1 1 1 1 1\n5\n1 0 1 0 1\n9\n0 1 1 0 0 0 1 1 0",
        "1\n0\n0\n2\n3"
    ),
    (
        "1\n4\n1 0 0 1",
        "1"
    ),
    (
        "1\n5\n1 1 0 0 1",
        "1"
    ),
    (
        "1\n6\n1 0 1 0 1 0",
        "2"
    ),
    (
        "1\n7\n0 0 1 0 1 0 0",
        "2"
    ),
    (
        "1\n3\n1 1 1",
        "0"
    ),
    (
        "1\n3\n0 1 1",
        "1"
    ),
    (
        "1\n3\n1 0 0",
        "1"
    ),
    (
        "1\n2\n1 0",
        "0"
    ),
    (
        "1\n2\n0 1",
        "0"
    )
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")