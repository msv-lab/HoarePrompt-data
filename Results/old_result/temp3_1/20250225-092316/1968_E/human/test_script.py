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
input_data_1 = "5\n2\n3\n4\n5\n6"
expected_output_1 = """2 2
2 1
3 3
3 1
3 3
2 3
3 1
4 4
4 3
1 1
1 3
1 4
2 1
5 5
1 4
1 5
1 6
5 2
5 5
6 1"""

assert run_program_with_captured_io(input_data_1) == expected_output_1

input_data_2 = "1\n2"
expected_output_2 = """2 2
2 1"""

assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = "1\n3"
expected_output_3 = """3 3
3 1
2 1"""

assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = "1\n4"
expected_output_4 = """4 4
4 3
1 1
1 3
4 4"""

assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = "1\n5"
expected_output_5 = """5 5
5 1
1 1
1 3
1 4
2 1
5 5"""

assert run_program_with_captured_io(input_data_5) == expected_output_5

input_data_6 = "1\n6"
expected_output_6 = """6 6
6 1
1 4
1 5
1 6
5 2
5 5
6 1"""

assert run_program_with_captured_io(input_data_6) == expected_output_6

print("All test cases passed!")