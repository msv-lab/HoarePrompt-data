# Import the helper function for capturing IO
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
input_data_1 = """7
4 4 5
5 5 9
10 10 5
5 5 11
1000000000 1000000000 1000000000
1000000000 1000000000 1
1000 1 1000"""
expected_output_1 = """17
35
100
45
1000000000000000000
1000000000000000000
500500"""

# Run the program with the input data and compare the output
assert run_program_with_captured_io(input_data_1) == expected_output_1

# Additional test cases
input_data_2 = """3
1 1 1
2 2 3
3 3 2"""
expected_output_2 = """1
5
8"""

assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = """1
10 5 15"""
expected_output_3 = """115"""

assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = """1
1 10 1"""
expected_output_4 = """10"""

assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = """1
1000000000 1 1000000000"""
expected_output_5 = """500000000500000000"""

assert run_program_with_captured_io(input_data_5) == expected_output_5

# End of script