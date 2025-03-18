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
test_cases = [
    # Test case 1
    {
        "input": "3\n1 1\n1\n2 2\n1\n2\n3 3\n7\n2\n3\n6\n1\n2\n1",
        "expected_output": "! 1\n? 1 1\n! -1\n? 1 9\n? 1 6\n? 3 6\n? 4 6\n! 6"
    },
    # Test case 2: Single element array
    {
        "input": "1\n1 1\n5",
        "expected_output": "! 5"
    },
    # Test case 3: No valid split
    {
        "input": "1\n2 2\n1\n2",
        "expected_output": "? 1 1\n? 2 1\n! -1"
    },
    # Test case 4: Valid split with multiple queries
    {
        "input": "1\n3 3\n1\n3\n6\n1\n2\n1",
        "expected_output": "? 1 9\n? 1 6\n? 3 6\n? 4 6\n! 6"
    },
    # Test case 5: Larger array with valid split
    {
        "input": "1\n5 2\n1\n2\n3\n4\n5",
        "expected_output": "? 1 10\n? 1 9\n? 1 8\n? 1 7\n? 1 6\n? 1 5\n? 1 4\n? 1 3\n? 1 2\n? 1 1\n! 5"
    },
    # Test case 6: Multiple test cases
    {
        "input": "2\n3 3\n1\n3\n6\n1\n2\n1\n2 2\n1\n2",
        "expected_output": "? 1 9\n? 1 6\n? 3 6\n? 4 6\n! 6\n? 1 1\n? 2 1\n! -1"
    }
]

# Run each test case
for i, test_case in enumerate(test_cases):
    result = run_program_with_captured_io(test_case["input"])
    expected_output = test_case["expected_output"]
    assert result == expected_output, f"Test case {i+1} failed: expected '{expected_output}', got '{result}'"

print("All test cases passed!")