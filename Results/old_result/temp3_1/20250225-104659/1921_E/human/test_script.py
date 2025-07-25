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
    ("1\n6 5 2 2 5 3\n", "Alice"),
    ("1\n4 1 2 1 4 1\n", "Bob"),
    ("1\n1 4 1 3 1 1\n", "Draw"),
    ("1\n5 5 1 4 5 2\n", "Draw"),
    ("1\n4 4 1 1 4 4\n", "Draw"),
    ("1\n10 10 1 6 10 8\n", "Alice"),
    ("1\n10 10 2 6 10 7\n", "Draw"),
    ("1\n10 10 9 1 8 1\n", "Draw"),
    ("1\n10 10 8 1 10 2\n", "Bob"),
    ("1\n10 10 1 1 2 1\n", "Alice"),
    ("1\n10 10 1 3 4 1\n", "Alice"),
    ("1\n10 10 3 1 1 1\n", "Draw"),
    # Additional edge cases
    ("1\n1 1 1 1 1 2\n", "Draw"),  # Alice and Bob cannot move
    ("1\n2 2 1 1 2 2\n", "Draw"),  # Alice and Bob cannot move towards each other
    ("1\n2 2 1 2 2 1\n", "Alice"), # Alice can move diagonally to win
    ("1\n3 3 1 1 3 3\n", "Draw"),  # Both can move but no winner
    ("1\n3 3 1 2 3 2\n", "Alice"), # Alice can move down to win
    ("1\n3 3 2 1 1 2\n", "Bob"),   # Bob can move up to win
    ("1\n1000000 1000000 1 1 1000000 1000000\n", "Draw"), # Large board, no winner
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")