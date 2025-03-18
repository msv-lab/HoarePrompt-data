import io
import sys
from program import func

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Test Case 1
input_data_1 = """4
10 1 3
10
10
0
6
7"""
expected_output_1 = "0 6 7"
output_1 = capture_output(func, input_data_1)
assert output_1 == expected_output_1, f"Expected {expected_output_1}, but got {output_1}"

# Test Case 2
input_data_2 = """4
10 2 4
4 10
4 7
6
4
2
7"""
expected_output_2 = "5 4 2 5"
output_2 = capture_output(func, input_data_2)
assert output_2 == expected_output_2, f"Expected {expected_output_2}, but got {output_2}"

# Test Case 3
input_data_3 = """1
1000000000 1 1
1000000000
1000000000
99999999"""
expected_output_3 = "99999999"
output_3 = capture_output(func, input_data_3)
assert output_3 == expected_output_3, f"Expected {expected_output_3}, but got {output_3}"

# Test Case 4
input_data_4 = """1
6 1 3
6
5
2
6
5"""
expected_output_4 = "1 5 4"
output_4 = capture_output(func, input_data_4)
assert output_4 == expected_output_4, f"Expected {expected_output_4}, but got {output_4}"

# Test Case 5 (Edge Case)
input_data_5 = """1
10 2 1
4 10
4 7
10"""
expected_output_5 = "7"
output_5 = capture_output(func, input_data_5)
assert output_5 == expected_output_5, f"Expected {expected_output_5}, but got {output_5}"

# Test Case 6 (Edge Case)
input_data_6 = """1
1 1 1
1
1
1"""
expected_output_6 = "1"
output_6 = capture_output(func, input_data_6)
assert output_6 == expected_output_6, f"Expected {expected_output_6}, but got {output_6}"

print("All tests passed!")