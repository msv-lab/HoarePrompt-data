# Include necessary imports if any
import io
import sys

# Helper function to automate input/output capture and execute `program.py` safely
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
input_data_1 = """6
3
000
011
011
4
0000
0000
0100
1110
2
11
11
5
00111
00010
00000
00000
00000
10
0000000000
0000000000
0000000000
0000000000
0000000000
1111111110
0111111100
0011111000
0001110000
0000100000
3
111
111
111"""

expected_output_1 = """SQUARE
TRIANGLE
SQUARE
TRIANGLE
TRIANGLE
SQUARE"""

# Run the program with the test input and capture the output
assert run_program_with_captured_io(input_data_1) == expected_output_1

# Additional test cases
input_data_2 = """2
4
0000
1111
1111
1111
3
001
011
111"""

expected_output_2 = """SQUARE
TRIANGLE"""

assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = """1
5
00100
01110
11111
01110
00100"""

expected_output_3 = """SQUARE"""

assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = """1
5
00100
00100
01110
00100
00100"""

expected_output_4 = """TRIANGLE"""

assert run_program_with_captured_io(input_data_4) == expected_output_4

# End of script