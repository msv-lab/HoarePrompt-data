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
input_data_1 = """4
7
1 1 1 1 1 1 1
4
3 2 1 3
3
1 2 3
1
1"""
expected_output_1 = """35
2
0
0"""

input_data_2 = """1
3
0 1 2"""
expected_output_2 = """0"""

input_data_3 = """1
6
0 0 0 0 0 0"""
expected_output_3 = """20"""

input_data_4 = """1
5
1 1 1 1 2"""
expected_output_4 = """10"""

input_data_5 = """1
10
1 2 3 4 5 6 7 8 9 10"""
expected_output_5 = """120"""

# Assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Additional edge cases
input_data_6 = """1
3
1 1 1"""
expected_output_6 = """1"""
assert run_program_with_captured_io(input_data_6) == expected_output_6

input_data_7 = """1
4
1 1 1 1"""
expected_output_7 = """4"""
assert run_program_with_captured_io(input_data_7) == expected_output_7

# End of script