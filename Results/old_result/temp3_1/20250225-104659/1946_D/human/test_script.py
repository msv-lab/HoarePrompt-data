# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call import it
from program import func_1

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

# Test case 1
arr = [1, 2, 3]
x = 1
assert func_1(arr, x) == 2

# Test case 2
arr = [1, 1]
x = 2
assert func_1(arr, x) == 2

# Test case 3
arr = [1, 3]
x = 2
assert func_1(arr, x) == 1

# Test case 4
arr = [1, 3]
x = 3
assert func_1(arr, x) == 2

# Test case 5
arr = [0, 0, 1]
x = 2
assert func_1(arr, x) == 3

# Test case 6
arr = [1, 3, 3, 7]
x = 2
assert func_1(arr, x) == -1

# Test case 7
arr = [2, 3]
x = 2
assert func_1(arr, x) == 1

# Test case 8
arr = [0, 1, 2, 2, 1]
x = 0
assert func_1(arr, x) == -1

# Test case 9 (single element array)
arr = [0]
x = 0
assert func_1(arr, x) == 1

# Test case 10 (all elements are the same)
arr = [2, 2, 2, 2]
x = 2
assert func_1(arr, x) == 4

# Test case 11 (no valid segmentation)
arr = [1, 2, 4, 8, 16]
x = 1
assert func_1(arr, x) == -1

# Test case 12 (large array with small x)
arr = [1] * 100000
x = 1
assert func_1(arr, x) == 100000

# Test case 13 (large array with large x)
arr = [1] * 100000
x = (1 << 30) - 1
assert func_1(arr, x) == 100000

# Test case 14 (alternating bits)
arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
x = 1023
assert func_1(arr, x) == 10

# Test case 15 (mixed values)
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 31
assert func_1(arr, x) == 10

# Test case 16 (edge case with x = 0)
arr = [0, 0, 0, 0]
x = 0
assert func_1(arr, x) == 4

# Test case 17 (edge case with x = 0 and non-zero values)
arr = [1, 2, 4, 8]
x = 0
assert func_1(arr, x) == -1

# End of script