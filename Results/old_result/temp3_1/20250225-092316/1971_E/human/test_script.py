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
# Test case 1 from the problem statement
input_data_1 = """4
10 1 3
10
10
0
6
7"""
expected_output_1 = "0 6 7"
assert run_program_with_captured_io(input_data_1) == expected_output_1

# Test case 2 from the problem statement
input_data_2 = """4
10 2 4
4 10
4 7
6
4
2
7"""
expected_output_2 = "5 4 2 5"
assert run_program_with_captured_io(input_data_2) == expected_output_2

# Test case 3 from the problem statement
input_data_3 = """4
1000000000 1 1
1000000000
1000000000
99999999"""
expected_output_3 = "99999999"
assert run_program_with_captured_io(input_data_3) == expected_output_3

# Test case 4 from the problem statement
input_data_4 = """4
6 1 3
6
5
2
6
5"""
expected_output_4 = "1 5 4"
assert run_program_with_captured_io(input_data_4) == expected_output_4

# Additional test case: Single segment, no delay
input_data_5 = """1
5 1 5
5
5
0
1
2
3
4"""
expected_output_5 = "0 1 2 3 4"
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Additional test case: Multiple segments with different speeds
input_data_6 = """1
10 2 5
3 10
2 5
1
2
3
4
5"""
expected_output_6 = "0 1 2 4 4"
assert run_program_with_captured_io(input_data_6) == expected_output_6

# Additional test case: Large input values
input_data_7 = """1
1000000000 1 1
1000000000
1000000000
500000000"""
expected_output_7 = "500000000"
assert run_program_with_captured_io(input_data_7) == expected_output_7

# End of script