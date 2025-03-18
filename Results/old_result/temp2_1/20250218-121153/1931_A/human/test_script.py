import io
import sys

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Import the function or the main logic from the provided program
from program import *

def test_program():
    # Test case 1: Minimum possible value
    input_data = "1\n3"
    expected_output = "aaa"
    assert capture_output(main, input_data) == expected_output, f"Failed for input {input_data}"

    # Test case 2: Example from the problem statement
    input_data = "5\n24\n70\n3\n55\n48"
    expected_output = "aav\nrzz\naaa\nczz\nauz"
    assert capture_output(main, input_data) == expected_output, f"Failed for input {input_data}"

    # Test case 3: Maximum possible value
    input_data = "1\n78"
    expected_output = "zzz"
    assert capture_output(main, input_data) == expected_output, f"Failed for input {input_data}"

    # Test case 4: Edge case where the sum is just above the minimum
    input_data = "1\n4"
    expected_output = "aab"
    assert capture_output(main, input_data) == expected_output, f"Failed for input {input_data}"

    # Test case 5: Edge case where the sum is just below the maximum
    input_data = "1\n77"
    expected_output = "yyz"
    assert capture_output(main, input_data) == expected_output, f"Failed for input {input_data}"

    # Test case 6: Middle values
    input_data = "3\n25\n30\n40"
    expected_output = "aaw\naaz\nabz"
    assert capture_output(main, input_data) == expected_output, f"Failed for input {input_data}"

    print("All test cases passed!")

# Run the test function
test_program()