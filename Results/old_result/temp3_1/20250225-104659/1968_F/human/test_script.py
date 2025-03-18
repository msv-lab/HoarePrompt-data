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
5 5
1 1 2 3 0
1 5
2 4
3 5
1 3
3 4
5 5
1 2 3 4 5
1 5
2 4
3 5
1 3
2 3
7 4
12 9 10 9 10 11 9
1 5
1 7
2 6
2 7
11 4
0 0 1 0 0 1 0 1 1 0 1
1 2
2 5
6 9
7 11"""

expected_output_1 = """YES
YES
NO
NO
NO
YES
NO
NO
YES
NO
NO
NO
NO
NO
YES
NO
YES
YES"""

# Run the program with the test input and capture the output
output_1 = run_program_with_captured_io(input_data_1)

# Assert that the output matches the expected output
assert output_1 == expected_output_1, f"Test case 1 failed: expected {expected_output_1}, got {output_1}"

# Additional test cases can be added here
input_data_2 = """1
3 3
1 2 3
1 2
2 3
1 3"""

expected_output_2 = """NO
NO
NO"""

output_2 = run_program_with_captured_io(input_data_2)
assert output_2 == expected_output_2, f"Test case 2 failed: expected {expected_output_2}, got {output_2}"

input_data_3 = """1
4 2
1 1 1 1
1 4
2 3"""

expected_output_3 = """YES
YES"""

output_3 = run_program_with_captured_io(input_data_3)
assert output_3 == expected_output_3, f"Test case 3 failed: expected {expected_output_3}, got {output_3}"

print("All test cases passed!")