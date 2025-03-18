# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

from program import *
import io
import sys

# Helper function to capture output
def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# # Test Case 1: Even n
# input_data = "2\n4\n3"
# expected_output = "4 1 2 3"
# out=  capture_output(func, input_data) 
# assert out == expected_output

# Test Case 2: Odd n
input_data = "1\n3"
expected_output = "1 2 3"
assert capture_output(func, input_data) == expected_output

# # Test Case 3: Larger n
# input_data = "2\n7\n"
# expected_output = "7 1 2 3 4 5 6"
# assert capture_output(func, input_data) == expected_output

# # Test Case 4: n close to upper limit
# input_data = "2\n100000\n"
# expected_output = "50000 1 2 3 ... 99999"  # Note: This is a conceptual representation, actual output might differ
# # Since the exact output is hard to predict without running, we can check if the pattern holds
# actual_output = capture_output(func, input_data)
# assert all(int(num) <= 100000 for num in actual_output.split())  # Check if all numbers are within the range
# assert len(actual_output.split()) == 100000  # Check if the length is correct

# # Test Case 5: Single test case with n = 3
# input_data = "1\n3\n"
# expected_output = "1 2 3"
# assert capture_output(func, input_data) == expected_output

# # Test Case 6: Single test case with n = 4
# input_data = "1\n4\n"
# expected_output = "4 1 2 3"
# assert capture_output(func, input_data) == expected_output

# # Test Case 7: Single test case with n = 5
# input_data = "1\n5\n"
# expected_output = "5 1 2 3 4"
# assert capture_output(func, input_data) == expected_output

# # Test Case 8: Single test case with n = 6
# input_data = "1\n6\n"
# expected_output = "6 1 2 3 4 5"
# assert capture_output(func, input_data) == expected_output

# # End of script