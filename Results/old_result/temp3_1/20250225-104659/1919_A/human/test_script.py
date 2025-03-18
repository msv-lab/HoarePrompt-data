# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

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
input_data_1 = """10\n1 1\n1 4\n5 3\n4 5\n11 9\n83 91\n1032 9307\n839204 7281\n1000000000 1000000000\n53110 2024"""
expected_output_1 = """Bob\nAlice\nBob\nAlice\nBob\nBob\nAlice\nAlice\nBob\nBob"""

assert run_program_with_captured_io(input_data_1) == expected_output_1

# Additional test cases
input_data_2 = """3\n2 2\n3 3\n4 4"""
expected_output_2 = """Bob\nBob\nBob"""
assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = """3\n1 2\n2 1\n3 4"""
expected_output_3 = """Alice\nAlice\nBob"""
assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = """1\n1000000000 1000000000"""
expected_output_4 = """Bob"""
assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = """1\n1 1000000000"""
expected_output_5 = """Alice"""
assert run_program_with_captured_io(input_data_5) == expected_output_5

input_data_6 = """1\n1000000000 1"""
expected_output_6 = """Bob"""
assert run_program_with_captured_io(input_data_6) == expected_output_6

# End of script