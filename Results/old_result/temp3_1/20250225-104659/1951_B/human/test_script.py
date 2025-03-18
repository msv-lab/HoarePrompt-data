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
        "3\n6 1\n12 10 14 11 8 3\n6 5\n7 2 727 10 12 13\n2 2\n1000000000 1",
        "1\n2\n0"
    ),
    (
        "1\n5 3\n1 2 3 4 5",
        "2"
    ),
    (
        "1\n5 3\n5 4 3 2 1",
        "0"
    ),
    (
        "1\n4 1\n10 20 30 40",
        "0"
    ),
    (
        "1\n4 4\n10 20 30 40",
        "3"
    ),
    (
        "1\n4 2\n10 40 20 30",
        "2"
    ),
    (
        "1\n4 2\n40 10 30 20",
        "1"
    ),
    (
        "1\n3 1\n1 2 3",
        "0"
    ),
    (
        "1\n3 2\n1 3 2",
        "1"
    ),
    (
        "1\n3 3\n3 2 1",
        "2"
    )
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")