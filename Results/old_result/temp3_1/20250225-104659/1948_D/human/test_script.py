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
    ("4\nzaabaabz\n?????\ncode?????s\ncodeforces\n", "6\n4\n10\n0"),
    ("1\naabbccdd\n", "2"),
    ("1\n??????\n", "6"),
    ("1\nabcde\n", "0"),
    ("1\nab?ba?\n", "4"),
    ("2\na?a?a?a?\n????????\n", "4\n8"),
    ("3\na?b?c?d?\n?a?b?c?d?\na?b?c?d?e?\n", "4\n4\n2"),
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")