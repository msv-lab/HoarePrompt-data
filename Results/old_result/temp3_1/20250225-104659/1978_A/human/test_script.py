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
input_data_1 = """5
2
1 1
4
2 3 3 1
5
2 2 3 2 2
2
10 3
3
1 2 3"""
expected_output_1 = """2
4
5
13
5"""

assert run_program_with_captured_io(input_data_1) == expected_output_1

input_data_2 = """1
3
1 2 3"""
expected_output_2 = """5"""
assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = """1
4
1 1 1 1"""
expected_output_3 = """2"""
assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = """1
2
1000000000 1000000000"""
expected_output_4 = """2000000000"""
assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = """1
5
1 1 2 2 3"""
expected_output_5 = """5"""
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Edge case: All books have the same number of pages
input_data_6 = """1
5
5 5 5 5 5"""
expected_output_6 = """10"""
assert run_program_with_captured_io(input_data_6) == expected_output_6

# Edge case: Two books with different number of pages
input_data_7 = """1
2
1 2"""
expected_output_7 = """3"""
assert run_program_with_captured_io(input_data_7) == expected_output_7

# Edge case: Minimum number of books
input_data_8 = """1
2
1 1000000000"""
expected_output_8 = """1000000001"""
assert run_program_with_captured_io(input_data_8) == expected_output_8

# End of script