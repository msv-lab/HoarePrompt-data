# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

from program import *

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test Case 1: Simple case with two books
# assert func() == 2

# # Test Case 2: Four books with two largest at the end
# assert func() == 4

# # Test Case 3: Five books with balanced distribution
# assert func() == 5

# # Test Case 4: Two books with large page difference
# assert func() == 13

# # Test Case 5: Three books in ascending order
# assert func() == 5

# Additional edge cases
# Test Case 6: Multiple test cases
import io
import sys

test_input = """5
2
1 1
4
2 3 3 1
5
2 2 3 2 2
2
10 3
3
1 2 3
"""

test_output = """2
4
5
13
5
"""

# Redirect stdin and stdout
sys.stdin = io.StringIO(test_input.strip())
sys.stdout = io.StringIO()

# Run the function
func()

# Check the output
result = sys.stdout.getvalue().strip()
assert result == test_output

# Reset stdin and stdout
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__

# End of script