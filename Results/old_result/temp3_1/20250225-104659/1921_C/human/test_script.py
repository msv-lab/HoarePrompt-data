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
        "6\n1 3 1 5\n3\n7 21 1 3\n4 6 10 13 17 20 26\n5 10 1 2\n1 2 3 4 5\n1 1000000000 1000000000 1000000000\n1000000000\n3 11 9 6\n6 8 10\n12 621526648 2585904 3566299\n51789 61859 71998 73401 247675 298086 606959 663464 735972 806043 806459 919683",
        "NO\nYES\nYES\nNO\nNO\nYES"
    ),
    (
        "1\n1 10 1 5\n10",
        "YES"
    ),
    (
        "1\n1 1 1 1\n1",
        "NO"
    ),
    (
        "1\n2 3 1 2\n1 2",
        "YES"
    ),
    (
        "1\n2 2 1 2\n1 2",
        "NO"
    ),
    (
        "1\n3 10 1 2\n1 5 10",
        "YES"
    ),
    (
        "1\n3 10 1 10\n1 5 10",
        "NO"
    ),
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")