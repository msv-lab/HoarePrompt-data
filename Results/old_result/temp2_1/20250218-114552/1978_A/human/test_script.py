# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

from program import func

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test Case 1: Two books with equal pages
assert func() == 2, "Test Case 1 Failed"

# Test Case 2: Four books with varying pages
assert func() == 4, "Test Case 2 Failed"

# Test Case 3: Five books with varying pages
assert func() == 5, "Test Case 3 Failed"

# Test Case 4: Two books with large pages
assert func() == 13, "Test Case 4 Failed"

# Test Case 5: Three books with consecutive pages
assert func() == 5, "Test Case 5 Failed"

# Additional edge cases
# Test Case 6: Two books with different pages
assert func() == 3, "Test Case 6 Failed"

# Test Case 7: Books with repeated pages
assert func() == 4, "Test Case 7 Failed"

# Test Case 8: Books with large values
assert func() == 1000000000 + 999999999, "Test Case 8 Failed"

# End of script