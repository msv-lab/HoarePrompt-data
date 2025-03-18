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
        "5\n1\n+\n5\n-----\n6\n+-+-+-\n10\n--+++++++-\n20\n+---++++-+++++---++-\n",
        "1\n5\n0\n4\n4"
    ),
    (
        "1\n10\n++++++++++\n",
        "10"
    ),
    (
        "1\n10\n----------\n",
        "10"
    ),
    (
        "1\n1\n-\n",
        "1"
    ),
    (
        "2\n2\n+-\n2\n-+\n",
        "0\n0"
    ),
    (
        "3\n3\n+++\n3\n---\n3\n+-+\n",
        "3\n3\n0"
    ),
    (
        "1\n5\n++--+\n",
        "2"
    ),
    (
        "1\n7\n++---++\n",
        "2"
    ),
    (
        "1\n9\n++----+++\n",
        "2"
    ),
    (
        "1\n11\n++------+++\n",
        "2"
    )
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")