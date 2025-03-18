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
input_data_1 = """4\n0 1\n12 4\n57 37\n316560849 14570961"""
expected_output_1 = """1\n8\n4\n33554432"""

input_data_2 = """1\n0 2"""
expected_output_2 = """1"""

input_data_3 = """1\n1 3"""
expected_output_3 = """1"""

input_data_4 = """1\n2 3"""
expected_output_4 = """2"""

input_data_5 = """1\n4 7"""
expected_output_5 = """1"""

# Run the program with the test cases and assert the outputs
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

print("All test cases passed!")