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
        "4\n2 1\n1 2 2 1\n6 1\n6 4 2 1 2 3 1 6 3 5 5 4\n4 1\n1 2 3 4 1 2 3 4\n6 2\n5 1 3 3 5 1 2 6 4 6 4 2",
        "2 1\n2 1\n6 4\n1 3\n1 2\n1 2\n5 1 3 3\n6 4 2 4"
    ),
    (
        "1\n4 2\n1 2 3 4 1 2 3 4",
        "1 2 3 4\n1 2 3 4"
    ),
    (
        "1\n6 1\n1 1 2 2 3 3 4 4 5 5 6 6",
        "1 1\n2 2"
    ),
    (
        "1\n8 4\n1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8",
        "1 2 3 4 5 6 7 8\n1 2 3 4 5 6 7 8"
    ),
    (
        "1\n10 5\n1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10",
        "1 2 3 4 5 6 7 8 9 10\n1 2 3 4 5 6 7 8 9 10"
    )
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    output = run_program_with_captured_io(input_data)
    assert output == expected_output, f"Test case {i+1} failed: expected {expected_output}, got {output}"
    print(f"Test case {i+1} passed.")