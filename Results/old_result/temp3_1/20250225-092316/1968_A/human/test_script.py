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
input_data_1 = "7\n10\n7\n21\n100\n2\n1000\n6"
expected_output_1 = "5\n6\n18\n98\n99\n1\n999"

input_data_2 = "3\n3\n4\n5"
expected_output_2 = "2\n3\n4"

input_data_3 = "1\n2"
expected_output_3 = "1"

input_data_4 = "2\n10\n2"
expected_output_4 = "5\n1"

# Run assertions
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4

print("All test cases passed!")