import io
import sys
from program import func_2

def run_program_with_captured_io(input_data):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        func_2()

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

def is_k_level_permutation(n, k, permutation):
    sums = [sum(permutation[i:i+k]) for i in range(n - k + 1)]
    return max(sums) - min(sums) <= 1

# Test cases
input_data_1 = "5\n2 2\n3 2\n10 4\n13 4\n7 4"
expected_output_1 = "2 1\n1 3 2\n1 8 4 10 2 7 5 9 3 6\n4 10 1 13 5 9 2 12 6 8 3 11 7\n1 6 3 7 2 5 4"
output_1 = run_program_with_captured_io(input_data_1)
assert output_1 == expected_output_1, f"Test case 1 failed: {output_1}"

# Additional test cases
input_data_2 = "1\n4 2"
expected_output_2 = "1 4 2 3"
output_2 = run_program_with_captured_io(input_data_2)
permutation_2 = list(map(int, output_2.split()))
assert is_k_level_permutation(4, 2, permutation_2), f"Test case 2 failed: {output_2}"

input_data_3 = "1\n6 4"
expected_output_3 = "1 6 2 5 3 4"
output_3 = run_program_with_captured_io(input_data_3)
permutation_3 = list(map(int, output_3.split()))
assert is_k_level_permutation(6, 4, permutation_3), f"Test case 3 failed: {output_3}"

input_data_4 = "1\n8 6"
expected_output_4 = "1 8 2 7 3 6 4 5"
output_4 = run_program_with_captured_io(input_data_4)
permutation_4 = list(map(int, output_4.split()))
assert is_k_level_permutation(8, 6, permutation_4), f"Test case 4 failed: {output_4}"

print("All test cases passed!")