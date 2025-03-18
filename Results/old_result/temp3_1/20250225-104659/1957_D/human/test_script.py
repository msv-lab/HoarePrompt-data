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
        "3\n3\n6 2 4\n1\n3\n5\n7 3 7 2 1",
        "4\n0\n16"
    ),
    (
        "1\n1\n1",
        "0"
    ),
    (
        "1\n2\n1 2",
        "1"
    ),
    (
        "1\n3\n1 1 1",
        "0"
    ),
    (
        "1\n4\n1 2 3 4",
        "6"
    ),
    (
        "1\n5\n1 2 4 8 16",
        "10"
    ),
    (
        "1\n6\n1 3 5 7 9 11",
        "15"
    ),
    (
        "1\n7\n1 1 1 1 1 1 1",
        "0"
    ),
    (
        "1\n8\n1 2 3 4 5 6 7 8",
        "21"
    ),
    (
        "1\n9\n1 2 3 4 5 6 7 8 9",
        "28"
    )
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")