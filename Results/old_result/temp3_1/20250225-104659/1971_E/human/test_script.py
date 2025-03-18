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
input_data_1 = """4
10 1 3
10
10
0
6
7
10 2 4
4 10
4 7
6
4
2
7
1000000000 1 1
1000000000
1000000000
99999999
6 1 3
6
5
2
6
5"""
expected_output_1 = """0 6 7
5 4 2 5
99999999
1 5 4"""

assert run_program_with_captured_io(input_data_1) == expected_output_1

# Additional test cases
input_data_2 = """1 1 1
1
1
0"""
expected_output_2 = """0"""
assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = """2 2 2
1 2
1 2
1
2"""
expected_output_3 = """1 2"""
assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = """5 3 3
1 3 5
1 3 5
1
3
5"""
expected_output_4 = """1 3 5"""
assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = """10 1 1
10
5
5"""
expected_output_5 = """5"""
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Edge case with large numbers
input_data_6 = """1000000000 1 1
1000000000
1000000000
999999999"""
expected_output_6 = """999999999"""
assert run_program_with_captured_io(input_data_6) == expected_output_6

print("All test cases passed.")