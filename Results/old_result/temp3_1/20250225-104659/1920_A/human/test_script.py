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
        "6\n4\n1 3\n2 10\n3 1\n3 5\n2\n1 5\n2 4\n10\n3 6\n3 7\n1 2\n1 7\n3 100\n3 44\n2 100\n2 98\n1 3\n3 99\n6\n1 5\n2 10\n1 9\n2 2\n3 2\n3 9\n5\n1 1\n2 2\n3 1\n3 2\n3 3\n6\n1 10000\n2 900000000\n3 500000000\n1 100000000\n3 10000\n3 900000001",
        "7\n0\n90\n0\n0\n800000000"
    ),
    (
        "1\n3\n1 1\n2 3\n3 2",
        "2"
    ),
    (
        "1\n3\n1 5\n2 5\n3 4",
        "1"
    ),
    (
        "1\n3\n1 1\n2 1\n3 1",
        "0"
    ),
    (
        "1\n3\n1 1\n2 2\n3 3",
        "0"
    ),
    (
        "1\n4\n1 1\n2 10\n3 5\n3 7",
        "6"
    )
]

# Run the tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")