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
        "3\n1 2\n4 5\n1 5\n4 2\n-1 1\n1 -1\n1 1\n-1 -1\n45 11\n45 39\n17 11\n17 39",
        "9\n4\n784"
    ),
    (
        "1\n0 0\n0 1\n1 1\n1 0",
        "1"
    ),
    (
        "2\n-2 -2\n-2 2\n2 2\n2 -2\n10 10\n10 20\n20 20\n20 10",
        "16\n100"
    ),
    (
        "1\n-5 -5\n-5 5\n5 5\n5 -5",
        "100"
    ),
    (
        "1\n100 100\n100 101\n101 101\n101 100",
        "1"
    )
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")