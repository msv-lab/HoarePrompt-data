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
input_data_1 = """3\n2\n2 1\n5\n1 100 1000 1000000 1000000000\n3\n6 4 8"""
expected_output_1 = """3 2\n1000000005 1000004 1003 102 2\n11 7 6"""

input_data_2 = """1\n1\n1"""
expected_output_2 = """2"""

input_data_3 = """1\n3\n1 2 3"""
expected_output_3 = """4 3 2"""

input_data_4 = """1\n3\n3 2 1"""
expected_output_4 = """4 3 2"""

input_data_5 = """1\n5\n1 1 1 1 1"""
expected_output_5 = """6"""

# Assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Additional edge case: large input
large_input = "1\n300000\n" + " ".join(str(i) for i in range(1, 300001))
large_expected_output = " ".join(str(i) for i in range(300001, 1, -1))
assert run_program_with_captured_io(large_input) == large_expected_output

# End of script