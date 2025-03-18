# Import the function from the provided program
from program import func

# Helper function to capture printed output
import io
import sys

def capture_output(func, input_data):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        func()

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Test cases
input_data_1 = """4\n2 5 9\n3 5 9\n3 5 11\n4 5 11"""
expected_output_1 = """9\n14\n15\n20"""

input_data_2 = """1\n1 10 15"""
expected_output_2 = """10"""

input_data_3 = """1\n2 10 15"""
expected_output_3 = """15"""

input_data_4 = """1\n3 10 15"""
expected_output_4 = """25"""

input_data_5 = """1\n4 10 15"""
expected_output_5 = """30"""

input_data_6 = """1\n5 10 15"""
expected_output_6 = """35"""

input_data_7 = """1\n100 1 2"""
expected_output_7 = """150"""

# Assertions
assert capture_output(func, input_data_1) == expected_output_1
assert capture_output(func, input_data_2) == expected_output_2
assert capture_output(func, input_data_3) == expected_output_3
assert capture_output(func, input_data_4) == expected_output_4
assert capture_output(func, input_data_5) == expected_output_5
assert capture_output(func, input_data_6) == expected_output_6
assert capture_output(func, input_data_7) == expected_output_7

# Additional edge cases
input_data_8 = """1\n1 30 50"""
expected_output_8 = """30"""

input_data_9 = """1\n2 30 50"""
expected_output_9 = """50"""

input_data_10 = """1\n3 30 50"""
expected_output_10 = """80"""

input_data_11 = """1\n4 30 50"""
expected_output_11 = """100"""

input_data_12 = """1\n5 30 50"""
expected_output_12 = """130"""

input_data_13 = """1\n100 30 50"""
expected_output_13 = """1500"""

# More assertions
assert capture_output(func, input_data_8) == expected_output_8
assert capture_output(func, input_data_9) == expected_output_9
assert capture_output(func, input_data_10) == expected_output_10
assert capture_output(func, input_data_11) == expected_output_11
assert capture_output(func, input_data_12) == expected_output_12
assert capture_output(func, input_data_13) == expected_output_13

# End of script