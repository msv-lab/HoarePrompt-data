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
input_data_1 = """6
5 1
1 2
1 3
3 4
3 5
2 1
1 2
6 1
1 2
2 3
3 4
4 5
5 6
3 1
1 2
1 3
8 2
1 2
1 3
2 4
2 5
3 6
3 7
3 8
6 2
1 2
2 3
1 4
4 5
5 6"""
expected_output_1 = """2
1
3
1
1
2"""

input_data_2 = """3
10 2
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
4 1
1 2
2 3
3 4
5 2
1 2
2 3
3 4
4 5"""
expected_output_2 = """3
1
2"""

input_data_3 = """1
7 3
1 2
2 3
3 4
4 5
5 6
6 7"""
expected_output_3 = """1"""

input_data_4 = """2
9 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
5 2
1 2
2 3
3 4
4 5"""
expected_output_4 = """2
2"""

# Run tests
assert run_program_with_captured_io(input_data_1) == expected_output_1
assert run_program_with_captured_io(input_data_2) == expected_output_2
assert run_program_with_captured_io(input_data_3) == expected_output_3
assert run_program_with_captured_io(input_data_4) == expected_output_4

print("All tests passed!")