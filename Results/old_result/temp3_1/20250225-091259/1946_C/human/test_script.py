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

assert run_program_with_captured_io(input_data_1) == expected_output_1

# Additional test cases
input_data_2 = """1
4 1
1 2
2 3
3 4"""
expected_output_2 = """2"""
assert run_program_with_captured_io(input_data_2) == expected_output_2

input_data_3 = """1
5 2
1 2
2 3
3 4
4 5"""
expected_output_3 = """2"""
assert run_program_with_captured_io(input_data_3) == expected_output_3

input_data_4 = """1
7 3
1 2
1 3
2 4
2 5
3 6
3 7"""
expected_output_4 = """2"""
assert run_program_with_captured_io(input_data_4) == expected_output_4

input_data_5 = """1
10 4
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10"""
expected_output_5 = """2"""
assert run_program_with_captured_io(input_data_5) == expected_output_5

# Edge case: Minimum n and k
input_data_6 = """1
3 1
1 2
2 3"""
expected_output_6 = """1"""
assert run_program_with_captured_io(input_data_6) == expected_output_6

# Edge case: Maximum n and k
input_data_7 = """1
100000 99999"""
# Constructing a simple path graph for this large input
edges = "\n".join(f"{i} {i+1}" for i in range(1, 100000))
input_data_7 += "\n" + edges
expected_output_7 = """1"""
assert run_program_with_captured_io(input_data_7) == expected_output_7

# End of script