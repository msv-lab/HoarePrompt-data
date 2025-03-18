import io
import sys

from program import *

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Test Case 1: Simple Tree
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
expected_output_1 = "2\n1\n3\n1\n1\n2"
output_1 = capture_output(func_5, input_data_1)
assert output_1 == expected_output_1, f"Expected {expected_output_1}, but got {output_1}"

# Test Case 2: Edge Case with Minimum k
input_data_2 = """1
4 1
1 2
1 3
1 4"""
expected_output_2 = "1"
output_2 = capture_output(func_5, input_data_2)
assert output_2 == expected_output_2, f"Expected {expected_output_2}, but got {output_2}"

# Test Case 3: Edge Case with Maximum k
input_data_3 = """1
4 2
1 2
1 3
1 4"""
expected_output_3 = "1"
output_3 = capture_output(func_5, input_data_3)
assert output_3 == expected_output_3, f"Expected {expected_output_3}, but got {output_3}"

# Test Case 4: Single Node Tree
input_data_4 = """1
1 0"""
expected_output_4 = "1"
output_4 = capture_output(func_5, input_data_4)
assert output_4 == expected_output_4, f"Expected {expected_output_4}, but got {output_4}"

# Test Case 5: Large Tree
input_data_5 = """1
10 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
expected_output_5 = "2"
output_5 = capture_output(func_5, input_data_5)
assert output_5 == expected_output_5, f"Expected {expected_output_5}, but got {output_5}"

# Test Case 6: Multiple Components After Removal
input_data_6 = """1
7 2
1 2
2 3
3 4
4 5
5 6
6 7"""
expected_output_6 = "2"
output_6 = capture_output(func_5, input_data_6)
assert output_6 == expected_output_6, f"Expected {expected_output_6}, but got {output_6}"

print("All tests passed!")