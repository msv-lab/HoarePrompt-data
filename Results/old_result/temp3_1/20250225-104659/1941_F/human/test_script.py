# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import func

# Otherwise use the run_program_with_captured_io(input_data) function to run the program and capture the output
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

# Write your test cases below
# Each test case should include assertions based on the problem description
# Example:
# assert function_name(input) == expected_output

# or if the program is a script we must execute 
# input_data = "input data"
# expected_output = "expected output"
# assert run_program_with_captured_io(input_data) == expected_output 

# Test cases
test_cases = [
    (
        """7
5 5 5
5 10 15 20 26
11 14 16 13 8
16 4 5 3 1
7 6 5
1 4 7 10 18 21 22
2 3 5 7 4 2
6 8 9 3 2
7 6 5
1 4 7 10 18 21 22
2 3 5 7 4 2
6 8 13 3 2
5 6 3
2 10 13 20 25
11 6 10 16 14 5
6 17 15
4 2 2
11 12 14 15
19 14
10 6
8 4 2
3 10 16 18 21 22 29 30
9 13 16 15
4 2
2 4 7
4 21
4 15 14 5
20 1 15 1 12 5 11""",
        """5
4
5
8
2
7
11"""
    ),
    (
        """1
3 3 3
1 5 10
2 3 4
1 2 3""",
        """2"""
    ),
    (
        """1
2 1 1
1 10
5
5""",
        """5"""
    ),
    (
        """1
4 2 2
1 4 7 10
2 8
3 6""",
        """3"""
    ),
    (
        """1
5 1 1
1 2 3 4 5
1
1""",
        """1"""
    )
]

for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")