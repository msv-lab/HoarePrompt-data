# Import the helper function to run the program and capture output
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
        "9\n2 2\n14 2\n3 5\n9 56 1\n4 10\n1 2007 800 1580\n4 5\n5000 123 30 4\n10 10\n6 4 6 2 3 1 10 9 10 7\n1 1\n6\n1 1\n10\n8 9\n1 2 9 10 10 2 10 2\n4 5\n10 10 10 10",
        "Sasha\nAnna\nAnna\nSasha\nSasha\nAnna\nAnna\nAnna\nSasha"
    ),
    (
        "1\n2 2\n14 2",
        "Sasha"
    ),
    (
        "1\n3 5\n9 56 1",
        "Anna"
    ),
    (
        "1\n4 10\n1 2007 800 1580",
        "Anna"
    ),
    (
        "1\n4 5\n5000 123 30 4",
        "Sasha"
    ),
    (
        "1\n10 10\n6 4 6 2 3 1 10 9 10 7",
        "Sasha"
    ),
    (
        "1\n1 1\n6",
        "Anna"
    ),
    (
        "1\n1 1\n10",
        "Anna"
    ),
    (
        "1\n8 9\n1 2 9 10 10 2 10 2",
        "Anna"
    ),
    (
        "1\n4 5\n10 10 10 10",
        "Anna"
    )
]

# Run the test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")