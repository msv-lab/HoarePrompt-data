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
input_data_1 = "3\n6\n1\n2"
expected_output_1 = "YES\nAAABAACC\nNO\nYES\nMM"

input_data_2 = "1\n2"
expected_output_2 = "YES\nAA"

input_data_3 = "1\n1"
expected_output_3 = "NO"

input_data_4 = "1\n50"
expected_output_4 = "YES\nAABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZAABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZAA"

input_data_5 = "2\n2\n50"
expected_output_5 = "YES\nAA\nYES\nAABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZAABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZAA"

# Run tests
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4
assert run_program_with_captured_io(input_data_5) == expected_output_5

print("All test cases passed!")