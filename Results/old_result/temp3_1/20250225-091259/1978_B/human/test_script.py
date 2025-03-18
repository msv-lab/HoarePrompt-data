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
    ("7\n4 4 5\n5 5 9\n10 10 5\n5 5 11\n1000000000 1000000000 1000000000\n1000000000 1000000000 1\n1000 1 1000",
     "17\n35\n100\n45\n1000000000000000000\n1000000000000000000\n500500"),
    ("1\n1 1 1", "1"),
    ("1\n1 1 2", "2"),
    ("1\n2 1 2", "3"),
    ("1\n2 2 1", "2"),
    ("1\n3 3 5", "14"),
    ("1\n10 1 10", "55"),
    ("1\n10 10 1", "100"),
    ("1\n100 100 100", "10000"),
    ("1\n1000000000 1 1000000000", "500000000500000000"),
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")