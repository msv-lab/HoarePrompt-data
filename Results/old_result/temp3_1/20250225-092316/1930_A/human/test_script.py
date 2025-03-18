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
input_data_1 = "3\n1\n2 3\n2\n1 1 2 1\n3\n1 1 1 1 1 1"
expected_output_1 = "2\n2\n3"

input_data_2 = "1\n5\n1 2 3 4 5 6"
expected_output_2 = "9"  # 1 + 3 + 5 = 9

input_data_3 = "1\n1\n10 20"
expected_output_3 = "10"

input_data_4 = "2\n2\n1 2 3 4\n3\n5 5 5 5 5 5"
expected_output_4 = "3\n15"

input_data_5 = "1\n2\n10000000 10000000"
expected_output_5 = "10000000"

# Assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

print("All test cases passed!")