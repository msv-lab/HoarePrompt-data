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
def test_program():
    # Test case 1: Given example in the problem statement
    input_data = "2\n4\n3"
    expected_output = "4 1 2 3\n1 2 3"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 2: Single test case with n=5
    input_data = "1\n5"
    expected_output = "5 1 2 3 4"  # One of the valid permutations
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 3: Multiple test cases with different n values
    input_data = "3\n6\n7\n8"
    expected_output = "6 1 2 3 4 5\n7 1 2 3 4 5 6\n8 1 2 3 4 5 6 7"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 4: Edge case with n=3
    input_data = "1\n3"
    expected_output = "1 2 3"  # All permutations are valid
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 5: Large n value
    input_data = "1\n100000"
    output = run_program_with_captured_io(input_data)
    output_list = list(map(int, output.split()))
    assert len(output_list) == 100000
    assert set(output_list) == set(range(1, 100001))  # Ensure all numbers from 1 to 100000 are present
    for i in range(len(output_list) - 1):
        for j in range(i + 1, len(output_list) - 1):
            assert not (output_list[i] % output_list[j] == 0 and output_list[i + 1] % output_list[j + 1] == 0), \
                f"Invalid permutation: {output_list[i]} divides {output_list[j]} and {output_list[i + 1]} divides {output_list[j + 1]}"

# Run tests
test_program()