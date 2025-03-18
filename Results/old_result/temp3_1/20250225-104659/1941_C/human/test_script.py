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
9
mmapnapie
9
azabazapi
8
mappppie
18
mapmapmapmapmapmap
1
p
11
pppiepieeee"""

expected_output_1 = """2
0
2
6
0
2"""

# Run the program with the test input and capture the output
output_1 = run_program_with_captured_io(input_data_1)

# Assert that the captured output matches the expected output
assert output_1 == expected_output_1, f"Expected {expected_output_1}, but got {output_1}"

# Additional test cases
input_data_2 = """3
5
apple
7
mapping
10
pieright"""

expected_output_2 = """0
1
2"""

output_2 = run_program_with_captured_io(input_data_2)
assert output_2 == expected_output_2, f"Expected {expected_output_2}, but got {output_2}"

input_data_3 = """4
3
pie
3
map
6
pipemap
6
pimape"""

expected_output_3 = """1
1
2
2"""

output_3 = run_program_with_captured_io(input_data_3)
assert output_3 == expected_output_3, f"Expected {expected_output_3}, but got {output_3}"

print("All test cases passed!")