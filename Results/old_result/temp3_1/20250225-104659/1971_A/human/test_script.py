import io
import sys
from program import func

def run_program_with_captured_io(input_data):
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
input_data_1 = """10\n1 9\n8 4\n1 4\n3 4\n2 0\n2 4\n6 9\n3 3\n0 0\n9 9"""
expected_output_1 = """9 1\n8 4\n4 1\n4 3\n2 0\n4 2\n9 6\n3 3\n0 0\n9 9"""

input_data_2 = """1\n5 5"""
expected_output_2 = """5 5"""

input_data_3 = """3\n0 9\n9 0\n3 7"""
expected_output_3 = """9 0\n9 0\n7 3"""

input_data_4 = """5\n1 2\n2 1\n3 4\n4 3\n5 6"""
expected_output_4 = """2 1\n2 1\n4 3\n4 3\n6 5"""

# Assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4

print("All test cases passed!")