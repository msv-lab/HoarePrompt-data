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
        "4\n4 6\n3 1 4 2\nLRRL\n5 1\n1 1 1 1 1\nLLLLL\n6 8\n1 2 3 4 5 6\nRLLLRR\n1 10000\n10000\nR",
        "0 2 4 1\n0 0 0 0 0\n0 0 0 4 4 4\n0"
    ),
    (
        "1\n3 7\n2 3 5\nLRR",
        "3 6 6"
    ),
    (
        "1\n2 10\n4 5\nRL",
        "0 4"
    ),
    (
        "1\n1 1\n1\nR",
        "0"
    ),
    (
        "2\n2 2\n1 1\nLL\n2 2\n1 2\nLR",
        "1\n1\n0\n0"
    ),
    (
        "1\n5 3\n1 2 3 4 5\nRRRRL",
        "0 0 0 0 0"
    ),
    (
        "1\n6 9\n9 8 7 6 5 4\nLRRLLR",
        "0 0 0 0 0 0"
    ),
    (
        "1\n4 13\n1 2 3 4\nLRLR",
        "2 6 5 8"
    ),
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")