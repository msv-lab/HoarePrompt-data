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


# Define a mock function to simulate the interaction with the interactor
def mock_func_1(a, b, c, d):
    # This function simulates the responses of the interactor
    # For simplicity, we assume a predefined permutation p
    # You can modify this function to simulate different permutations
    p = {0: 0, 1: 3, 2: 1, 3: 2}  # Example permutation for n=4
    x = p[a] | p[b]
    y = p[c] | p[d]
    if x < y:
        return '<'
    elif x > y:
        return '>'
    else:
        return '='

# Overwrite the func_1 in the program with our mock function
from program import func_1
program.func_1 = mock_func_1

# Test cases
# Test case 1
input_data_1 = """2
4
?
0 2 3 1
<
?
1 1 2 3
=
?
1 2 0 3
>
2
"""
expected_output_1 = """? 0 2 3 1
? 1 1 2 3
? 1 2 0 3
! 3 2
! 0 1"""

assert run_program_with_captured_io(input_data_1) == expected_output_1

# Test case 2
input_data_2 = """1
2
"""
expected_output_2 = """! 0 1"""

# Modify the mock function to simulate a different permutation for n=2
def mock_func_1_n2(a, b, c, d):
    p = {0: 0, 1: 1}  # Example permutation for n=2
    x = p[a] | p[b]
    y = p[c] | p[d]
    if x < y:
        return '<'
    elif x > y:
        return '>'
    else:
        return '='

program.func_1 = mock_func_1_n2

assert run_program_with_captured_io(input_data_2) == expected_output_2

# Test case 3
input_data_3 = """1
3
?
0 1 1 2
>
?
0 1 0 2
>
"""
expected_output_3 = """? 0 1 1 2
? 0 1 0 2
! 0 1"""

# Modify the mock function to simulate a different permutation for n=3
def mock_func_1_n3(a, b, c, d):
    p = {0: 0, 1: 2, 2: 1}  # Example permutation for n=3
    x = p[a] | p[b]
    y = p[c] | p[d]
    if x < y:
        return '<'
    elif x > y:
        return '>'
    else:
        return '='

program.func_1 = mock_func_1_n3

assert run_program_with_captured_io(input_data_3) == expected_output_3

# Test case 4: Larger permutation
input_data_4 = """1
5
?
0 1 2 3
>
?
0 1 0 4
>
?
0 2 0 4
>
?
0 3 0 4
>
?
0 4 1 2
>
?
0 4 1 3
>
?
0 4 2 3
>
"""
expected_output_4 = """? 0 1 2 3
? 0 1 0 4
? 0 2 0 4
? 0 3 0 4
? 0 4 1 2
? 0 4 1 3
? 0 4 2 3
! 0 4"""

# Modify the mock function to simulate a different permutation for n=5
def mock_func_1_n5(a, b, c, d):
    p = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}  # Example permutation for n=5
    x = p[a] | p[b]
    y = p[c] | p[d]
    if x < y:
        return '<'
    elif x > y:
        return '>'
    else:
        return '='

program.func_1 = mock_func_1_n5

assert run_program_with_captured_io(input_data_4) == expected_output_4

# End of script