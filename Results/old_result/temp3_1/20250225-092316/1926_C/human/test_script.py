# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.
from program import func_1

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

# Test the function func_1
assert func_1(12) == 3  # 1 + 2 = 3
assert func_1(1) == 1   # 1 = 1
assert func_1(2) == 2   # 2 = 2
assert func_1(3) == 3   # 3 = 3
assert func_1(1434) == 12  # 1 + 4 + 3 + 4 = 12
assert func_1(2024) == 8  # 2 + 0 + 2 + 4 = 8
assert func_1(200000) == 2  # 2 + 0 + 0 + 0 + 0 + 0 = 2

# Simulate the full program's behavior
def calculate_sum_of_digit_sums(n):
    return sum(func_1(i) for i in range(1, n + 1))

# Test the full program's behavior with multiple test cases
input_data = """7
12
1
2
3
1434
2024
200000"""
expected_output = """51
1
3
6
18465
28170
4600002"""

# Capture the output of the program with the given input
output = run_program_with_captured_io(input_data)

# Assert that the captured output matches the expected output
assert output == expected_output

# Additional test cases
assert calculate_sum_of_digit_sums(12) == 51
assert calculate_sum_of_digit_sums(1) == 1
assert calculate_sum_of_digit_sums(2) == 3
assert calculate_sum_of_digit_sums(3) == 6
assert calculate_sum_of_digit_sums(1434) == 18465
assert calculate_sum_of_digit_sums(2024) == 28170
assert calculate_sum_of_digit_sums(200000) == 4600002

# End of script