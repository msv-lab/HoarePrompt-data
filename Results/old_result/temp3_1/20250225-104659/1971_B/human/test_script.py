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
    ("1\ncodeforces\n", "YES\nacdeforss"),
    ("1\naaaaa\n", "NO"),
    ("1\nxxxxy\n", "YES\nxyxxx"),
    ("1\nco\n", "YES\noc"),
    ("1\nd\n", "NO"),
    ("1\nnutdealer\n", "YES\naelddnrtu"),
    ("1\nmwistht\n", "YES\nhimsttw"),
    ("1\nhhhhhhhhhh\n", "NO"),
    ("3\na\nb\nab\n", "NO\nNO\nYES\nab"),
    ("2\nabc\ndef\n", "YES\nabc\nYES\ndef"),
    ("2\naaa\naab\n", "NO\nYES\naab"),
    ("4\nzzz\nzzzz\nzzzzz\nzzzzzz\n", "NO\nNO\nNO\nNO"),
    ("5\nabcd\nefgh\nijkl\nmnop\nqrst\n", "YES\nabcd\nYES\nefgh\nYES\nijkl\nYES\nmnop\nYES\nqrst"),
    ("1\nabcdefghij\n", "YES\nabcdefghij"),  # This should still be YES since sorting gives a different permutation
]

# Run test cases
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")