# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

from program import *

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test Case 1
def test_case_1():
    t = 5
    cases = [
        (2, [1, 1], 2),
        (4, [2, 3, 3, 1], 4),
        (5, [2, 2, 3, 2, 2], 5),
        (2, [10, 3], 13),
        (3, [1, 2, 3], 5)
    ]
    for n, pages, expected in cases:
        result = solution(n, pages)
        assert result == expected, f"Failed for {n} pages: {pages}, Expected: {expected}, Got: {result}"

# Add multiple test cases to ensure correctness across edge cases

# Helper function to simulate input for testing
def simulate_input(test_cases):
    for case in test_cases:
        t, pages = case
        sys.stdin = io.StringIO(f"{t}\n{len(pages)} {' '.join(map(str, pages))}")
        test_case_1()

# Import necessary modules for testing
import sys
import io

# Simulate input and run tests
simulate_input([
    (2, [1, 1]),
    (4, [2, 3, 3, 1]),
    (5, [2, 2, 3, 2, 2]),
    (2, [10, 3]),
    (3, [1, 2, 3])
])

# End of script