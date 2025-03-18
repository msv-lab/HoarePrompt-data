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
        "5\n5\n1 2 3 4 5\n8\n8 2 3 1 1 7 4 3\n5\n3 3 3 3 3\n1\n1\n2\n2 1",
        "3\n1\n0\n0\n0"
    ),
    (
        "1\n3\n1 3 2",
        "1"
    ),
    (
        "1\n4\n4 3 2 1",
        "0"
    ),
    (
        "1\n6\n1 2 3 4 5 6",
        "5"
    ),
    (
        "1\n2\n2 1",
        "0"
    ),
    (
        "1\n1\n1",
        "0"
    ),
    (
        "1\n10\n1 2 3 4 5 6 7 8 9 10",
        "9"
    ),
    (
        "1\n10\n10 9 8 7 6 5 4 3 2 1",
        "0"
    ),
    (
        "1\n10\n1 10 2 9 3 8 4 7 5 6",
        "4"
    ),
]

# Run the test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")