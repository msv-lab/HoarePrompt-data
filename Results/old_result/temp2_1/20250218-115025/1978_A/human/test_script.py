# This script contains test cases to validate the correctness of the provided solution in 'program.py'.

from program import func
import io
import sys

# Function to capture the output of the func when it's run
def capture_output(func, input_data):
    # Redirect stdin and stdout
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    func()

    # Reset stdout
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Test cases
def test_func():
    # Test Case 1
    input_data = """5
2
1 1
4
2 3 3 1
5
2 2 3 2 2
2
10 3
3
1 2 3"""
    expected_output = "2\n4\n5\n13\n5"
    assert capture_output(func, input_data) == expected_output, "Test Case 1 Failed"

    # Test Case 2: Single test case with minimum values
    input_data = """1
2
1 1"""
    expected_output = "2"
    assert capture_output(func, input_data) == expected_output, "Test Case 2 Failed"

    # Test Case 3: Single test case with large values
    input_data = """1
2
1000000000 1000000000"""
    expected_output = "2000000000"
    assert capture_output(func, input_data) == expected_output, "Test Case 3 Failed"

    # Test Case 4: Maximum number of books
    input_data = """1
100\n""" + " ".join(map(str, [i for i in range(1, 101)]))
    expected_output = "199"
    assert capture_output(func, input_data) == expected_output, "Test Case 4 Failed"

    # Test Case 5: Edge case with all identical values
    input_data = """1
4
5 5 5 5"""
    expected_output = "10"
    assert capture_output(func, input_data) == expected_output, "Test Case 5 Failed"

    # Test Case 6: Multiple test cases with varied values
    input_data = """3
2
1 2
3
1 2 3
4
1 2 3 4"""
    expected_output = "3\n5\n7"
    assert capture_output(func, input_data) == expected_output, "Test Case 6 Failed"

    print("All test cases passed!")

# Run the test cases
test_func()