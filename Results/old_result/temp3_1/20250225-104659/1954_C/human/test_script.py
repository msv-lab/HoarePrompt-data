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
input_data_1 = """3\n73\n31\n2\n5\n3516\n3982"""
expected_output_1 = """71\n33\n5\n2\n3912\n3586"""

input_data_2 = """1\n123\n987"""
expected_output_2 = """183\n927"""

input_data_3 = """1\n111\n111"""
expected_output_3 = """111\n111"""

input_data_4 = """1\n987654321\n123456789"""
expected_output_4 = """123454321\n987656789"""

input_data_5 = """2\n123456789\n987654321\n987654321\n123456789"""
expected_output_5 = """123454321\n987656789\n987654321\n123456789"""

# Assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Additional test cases
input_data_6 = """1\n19\n91"""
expected_output_6 = """19\n91"""

input_data_7 = """1\n222222222\n222222222"""
expected_output_7 = """222222222\n222222222"""

input_data_8 = """1\n13579\n97531"""
expected_output_8 = """13551\n97979"""

# Assertions for additional test cases
assert run_program_with_captured_io(input_data_6) == expected_output_6
assert run_program_with_captured_io(input_data_7) == expected_output_7
assert run_program_with_captured_io(input_data_8) == expected_output_8

# End of script