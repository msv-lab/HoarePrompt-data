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
        "11\n7 1\n7 2\n7 3\n7 4\n7 5\n7 6\n7 7\n1 1\n34 14\n84 19\n1000000000 1000000000",
        "1\n3\n5\n7\n2\n6\n4\n1\n27\n37\n536870912"
    ),
    (
        "1\n1 1",
        "1"
    ),
    (
        "1\n2 1",
        "1"
    ),
    (
        "1\n2 2",
        "2"
    ),
    (
        "1\n3 1",
        "1"
    ),
    (
        "1\n3 2",
        "3"
    ),
    (
        "1\n3 3",
        "2"
    ),
    (
        "1\n4 1",
        "1"
    ),
    (
        "1\n4 2",
        "3"
    ),
    (
        "1\n4 3",
        "2"
    ),
    (
        "1\n4 4",
        "4"
    ),
    (
        "1\n5 1",
        "1"
    ),
    (
        "1\n5 2",
        "3"
    ),
    (
        "1\n5 3",
        "5"
    ),
    (
        "1\n5 4",
        "2"
    ),
    (
        "1\n5 5",
        "4"
    ),
    (
        "1\n6 1",
        "1"
    ),
    (
        "1\n6 2",
        "3"
    ),
    (
        "1\n6 3",
        "5"
    ),
    (
        "1\n6 4",
        "2"
    ),
    (
        "1\n6 5",
        "6"
    ),
    (
        "1\n6 6",
        "4"
    ),
    (
        "1\n10 1",
        "1"
    ),
    (
        "1\n10 2",
        "3"
    ),
    (
        "1\n10 3",
        "5"
    ),
    (
        "1\n10 4",
        "7"
    ),
    (
        "1\n10 5",
        "9"
    ),
    (
        "1\n10 6",
        "2"
    ),
    (
        "1\n10 7",
        "6"
    ),
    (
        "1\n10 8",
        "10"
    ),
    (
        "1\n10 9",
        "4"
    ),
    (
        "1\n10 10",
        "8"
    )
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    result = run_program_with_captured_io(input_data)
    assert result == expected_output, f"Test case {i+1} failed: expected {expected_output}, got {result}"
    print(f"Test case {i+1} passed.")