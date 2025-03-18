import io
import sys

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

from program import func

# Test cases
def test_func():
    # Test case 1
    input_data = "7\n10\n7\n21\n100\n2\n1000\n6"
    expected_output = "5\n6\n18\n98\n1\n750\n3"
    assert capture_output(func, input_data) == expected_output

    # Test case 2: Single test case with minimum value
    input_data = "1\n2"
    expected_output = "1"
    assert capture_output(func, input_data) == expected_output

    # Test case 3: Single test case with a prime number
    input_data = "1\n11"
    expected_output = "10"
    assert capture_output(func, input_data) == expected_output

    # Test case 4: Single test case with a composite number
    input_data = "1\n25"
    expected_output = "20"
    assert capture_output(func, input_data) == expected_output

    # Test case 5: Multiple test cases with various values
    input_data = "4\n15\n20\n25\n30"
    expected_output = "14\n18\n20\n27"
    assert capture_output(func, input_data) == expected_output

    # Test case 6: Edge case with the maximum allowed value
    input_data = "1\n1000"
    expected_output = "750"
    assert capture_output(func, input_data) == expected_output

    print("All test cases passed!")

# Run the test function
test_func()