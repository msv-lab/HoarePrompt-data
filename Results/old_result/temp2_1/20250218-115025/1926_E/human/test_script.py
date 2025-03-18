# Import the function to test
from program import func

# Function to simulate input and capture output
import io
import sys

def test_func(test_input, expected_output):
    # Redirect stdin to simulate input
    sys.stdin = io.StringIO(test_input)
    
    # Redirect stdout to capture output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Run the function
    func()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # Check the output
    assert captured_output.getvalue().strip() == expected_output.strip()

# Test cases based on the problem description
test_func("11\n7 1\n7 2\n7 3\n7 4\n7 5\n7 6\n7 7\n1 1\n34 14\n84 19\n1000000000 1000000000",
          "1\n3\n5\n7\n2\n6\n4\n1\n27\n37\n536870912")

# Additional test cases to cover edge cases and larger inputs
test_func("3\n1 1\n2 1\n2 2",
          "1\n1\n2")

test_func("1\n100 50",
          "99")

test_func("1\n10 10",
          "8")

test_func("1\n1000000000 1",
          "1")

# End of script