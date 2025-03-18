# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# Since the provided program is a script, we need to use the run_program_with_captured_io function
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

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test case 1
input_data = """3
8 4 0
1 6 2 5
8 8 0
1 3 2 5 4 6 7 8
4 2 0
1 3"""
expected_output = """2
6
2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2: All vertices are chosen, forming a full triangulation
input_data = """1
5 5 0
1 2 3 4 5"""
expected_output = """3"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: Minimum number of vertices
input_data = """1
4 2 0
1 3"""
expected_output = """2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: No additional vertices can be chosen, but more triangles can be formed
input_data = """1
6 3 0
1 4 6"""
expected_output = """2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Vertices are chosen such that no additional triangles can be formed
input_data = """1
6 4 0
1 2 5 6"""
expected_output = """2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Large number of vertices with only a few chosen
input_data = """1
10 3 0
1 5 9"""
expected_output = """2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7: Vertices are chosen in a way that maximizes the number of triangles
input_data = """1
10 6 0
1 3 5 7 9 10"""
expected_output = """5"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 8: Vertices are chosen in a cyclic manner
input_data = """1
10 5 0
1 2 4 7 9"""
expected_output = """3"""
assert run_program_with_captured_io(input_data) == expected_output

# End of script