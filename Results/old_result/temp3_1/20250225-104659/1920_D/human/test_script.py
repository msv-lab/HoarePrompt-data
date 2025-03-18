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
        "4\n5 10\n1 1\n1 2\n2 1\n1 3\n2 3\n1 2 3 4 5 6 14 15 16 20\n10 10\n1 3\n1 8\n2 15\n1 6\n1 9\n1 1\n2 6\n1 1\n2 12\n2 10\n32752 25178 3198 3199 2460 2461 31450 33260 9016 4996\n12 5\n1 6\n1 11\n2 392130334\n1 4\n2 744811750\n1 10\n1 5\n2 209373780\n2 178928984\n1 3\n2 658326464\n2 1000000000\n914576963034536490 640707385283752918 636773368365261971 584126563607944922 1000000000000000000\n2 2\n1 1\n1 2\n1 2",
        "1 2 1 2 3 1 2 3 1 3\n9 8 1 3 1 3 6 3 8 8\n11 11 11 10 11\n1 2"
    ),
    (
        "1\n3 3\n1 1\n1 2\n2 1\n1 3\n3 1 2 3",
        "1 2 3"
    ),
    (
        "1\n4 4\n1 1\n1 2\n2 1\n1 3\n2 2\n4 5 6 7",
        "1 2 1 2 3"
    ),
    (
        "1\n2 2\n1 1\n1 2\n2 1\n1 3\n2 2\n3 4 5",
        "1 2 1 2"
    ),
    (
        "1\n1 1\n1 1\n1 1",
        "1"
    ),
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")