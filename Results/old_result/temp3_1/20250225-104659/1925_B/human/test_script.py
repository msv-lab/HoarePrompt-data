# Import the function from the provided program
from program import func

# Define a helper function to capture the printed output of the function
import io
import sys

def capture_printed_output(func, input_data):
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        # Simulate input using StringIO
        input_generator = iter(input_data.split('\n'))
        input_function = lambda: next(input_generator)
        func.__globals__['input'] = input_function
        
        # Call the function
        func()
        
        # Get the captured output
        return captured_output.getvalue().strip()
    finally:
        sys.stdout = original_stdout

# Test cases
test_cases = [
    (
        "3\n10 3\n5 5\n420 69",
        "2\n1\n6"
    ),
    (
        "1\n1 1",
        "1"
    ),
    (
        "1\n100 10",
        "10"
    ),
    (
        "1\n100 1",
        "100"
    ),
    (
        "1\n99999999 99999999",
        "1"
    ),
    (
        "1\n100000000 100000000",
        "1"
    ),
    (
        "1\n100000000 1",
        "100000000"
    ),
    (
        "1\n50 5",
        "10"
    ),
    (
        "1\n7 3",
        "1"
    ),
    (
        "1\n12 4",
        "3"
    )
]

# Run assertions for each test case
for i, (input_data, expected_output) in enumerate(test_cases):
    assert capture_printed_output(func, input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")