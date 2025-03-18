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
    ("8\nABABB\nABABA\nBBBAB\nAAAAA\nBBBBB\nBABAA\nAAAAB\nBAAAA", "B\nA\nB\nA\nB\nA\nA\nA"),
    ("1\nAAAAA", "A"),
    ("1\nBBBBB", "B"),
    ("1\nABABB", "B"),
    ("1\nABABA", "A"),
    ("1\nBBBAB", "B"),
    ("1\nBABAA", "A"),
    ("1\nAAAAB", "A"),
    ("1\nBAAAA", "A"),
    ("2\nAAAAA\nBBBBB", "A\nB"),
    ("2\nABABB\nABABA", "B\nA"),
    ("3\nBBBAB\nAAAAA\nBBBBB", "B\nA\nB"),
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")