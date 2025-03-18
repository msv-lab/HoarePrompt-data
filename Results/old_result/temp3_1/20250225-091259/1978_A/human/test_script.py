# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

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

# Test case 1
input_data = "5\n2\n1 1\n4\n2 3 3 1\n5\n2 2 3 2 2\n2\n10 3\n3\n1 2 3"
expected_output = "2\n4\n5\n13\n5"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2: All books have the same number of pages
input_data = "1\n4\n5 5 5 5"
expected_output = "10"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: Two books with different number of pages
input_data = "1\n2\n1 10"
expected_output = "11"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: Three books with different number of pages
input_data = "1\n3\n1 2 3"
expected_output = "5"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Large number of books with varying page counts
input_data = "1\n100\n" + " ".join(map(str, range(1, 101)))
expected_output = "200"
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Maximum number of test cases with minimum number of books
input_data = "500\n" + "\n".join(["2\n1 1"] * 500)
expected_output = "2\n" * 500
assert run_program_with_captured_io(input_data) == expected_output.strip()

# End of script