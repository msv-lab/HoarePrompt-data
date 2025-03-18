import io
import sys

def run_program_with_captured_io(input_data, fox_responses):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Mock the input function to return fox_responses
        def mock_input():
            return fox_responses.pop(0)

        original_input = __builtins__.input
        __builtins__.input = mock_input

        with open("program.py", "r", encoding="utf-8") as f:
            code = f.read()
            exec(code, {})

        __builtins__.input = original_input

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Define test cases
test_cases = [
    {
        "input": "3\n1 1\n",
        "fox_responses": ["1"],
        "expected_output": "! 1"
    },
    {
        "input": "3\n2 2\n",
        "fox_responses": ["1", "2"],
        "expected_output": "? 1 1\n? 2 1\n! -1"
    },
    {
        "input": "3\n6 3\n",
        "fox_responses": ["7", "2", "4", "6", "7", "6", "1"],
        "expected_output": "? 1 9\n? 1 6\n? 3 6\n? 4 6\n! 6"
    },
    {
        "input": "2\n5 3\n",
        "fox_responses": ["5", "3", "5", "5", "3", "5", "5"],
        "expected_output": "? 1 15\n? 1 10\n? 3 10\n? 4 10\n! 10\n? 1 15\n? 1 10\n? 3 10\n? 4 10\n! 10"
    },
    {
        "input": "1\n3 1\n",
        "fox_responses": ["3"],
        "expected_output": "! 3"
    }
]

# Run test cases
for i, test_case in enumerate(test_cases):
    input_data = test_case["input"]
    fox_responses = test_case["fox_responses"]
    expected_output = test_case["expected_output"]
    
    actual_output = run_program_with_captured_io(input_data, fox_responses)
    
    # Replace newlines for easier comparison
    actual_output = actual_output.replace('\n', ' ')
    expected_output = expected_output.replace('\n', ' ')
    
    assert actual_output == expected_output, f"Test case {i+1} failed: expected '{expected_output}', got '{actual_output}'"

print("All test cases passed!")