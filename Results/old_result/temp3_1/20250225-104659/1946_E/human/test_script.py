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
        "6\n1 1 1\n1\n1\n4 2 3\n1 2\n2 3 4\n3 3 1\n1 2 3\n3\n5 3 4\n1 2 3\n2 3 4 5\n20 5 4\n1 2 3 4 12\n12 13 18 20\n6 2 3\n1 3\n3 4 6",
        "1\n3\n1\n0\n317580808\n10"
    ),
    (
        "1\n3 2 2\n1 3\n1 3",
        "1"
    ),
    (
        "1\n3 2 2\n1 2\n2 3",
        "1"
    ),
    (
        "1\n4 2 2\n1 4\n1 4",
        "1"
    ),
    (
        "1\n4 3 3\n1 2 4\n2 3 4",
        "1"
    ),
    (
        "1\n5 3 3\n1 3 5\n3 4 5",
        "1"
    ),
    (
        "1\n5 2 2\n1 5\n1 5",
        "1"
    ),
    (
        "1\n5 2 2\n1 3\n3 5",
        "0"
    ),
    (
        "1\n5 2 2\n1 4\n2 5",
        "0"
    ),
    (
        "1\n5 2 2\n1 2\n4 5",
        "0"
    ),
    (
        "1\n6 2 2\n1 6\n1 6",
        "1"
    ),
    (
        "1\n6 2 2\n1 3\n3 6",
        "0"
    ),
    (
        "1\n6 2 2\n1 4\n4 6",
        "0"
    ),
    (
        "1\n6 2 2\n1 5\n5 6",
        "0"
    ),
    (
        "1\n6 2 2\n1 2\n5 6",
        "0"
    ),
    (
        "1\n6 2 2\n1 2\n4 5",
        "0"
    ),
    (
        "1\n6 2 2\n1 2\n3 6",
        "0"
    ),
    (
        "1\n6 2 2\n1 2\n2 5",
        "0"
    ),
    (
        "1\n6 2 2\n1 2\n2 4",
        "0"
    ),
    (
        "1\n6 2 2\n1 2\n2 3",
        "0"
    ),
    (
        "1\n6 3 3\n1 3 6\n3 4 6",
        "1"
    ),
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")