# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

# If there is a specific function we can call, import it
from program import func_1

# otherwise use the run_program_with_captured_io(input_data) function to run the program and capture the output

# Write your test cases below
# Each test case should include assertions based on the problem description
# Example:
# assert function_name(input) == expected_output

# Test case 1
n = 3
c = 2
d = 3
l = [3, 9, 6, 5, 7, 1, 10, 4, 8]
assert func_1(n, c, d, l) == 'NO'

# Test case 2
n = 3
c = 2
d = 3
l = [3, 9, 6, 5, 7, 1, 11, 4, 8]
assert func_1(n, c, d, l) == 'YES'

# Test case 3
n = 2
c = 100
d = 100
l = [400, 300, 400, 500]
assert func_1(n, c, d, l) == 'YES'

# Test case 4
n = 3
c = 2
d = 3
l = [3, 9, 6, 6, 5, 1, 11, 4, 8]
assert func_1(n, c, d, l) == 'NO'

# Test case 5
n = 4
c = 4
d = 4
l = [15, 27, 7, 19, 23, 23, 11, 15, 7, 3, 19, 23, 11, 15, 11, 15]
assert func_1(n, c, d, l) == 'NO'

# Test case 6: Edge case with minimum n
n = 2
c = 1
d = 1
l = [1, 4, 2, 3]
assert func_1(n, c, d, l) == 'YES'

# Test case 7: Edge case with maximum n
n = 500
c = 10**6
d = 10**6
l = list(range(1, n*n + 1))
# The last element minus the first element should be (n-1)*(c+d)
l[-1] = l[0] + (n-1)*(c+d)
assert func_1(n, c, d, l) == 'YES'

# Test case 8: All elements are the same
n = 3
c = 2
d = 3
l = [5, 5, 5, 5, 5, 5, 5, 5, 5]
assert func_1(n, c, d, l) == 'NO'

# Test case 9: Only two distinct elements
n = 2
c = 1
d = 1
l = [1, 2, 1, 2]
assert func_1(n, c, d, l) == 'NO'

# Test case 10: Large numbers
n = 3
c = 10**6
d = 10**6
l = [1, 10**9, 1 + (n-1)*(c+d), 1 + (n-1)*c, 1 + (n-1)*d, 1 + c + d, 1 + c, 1 + d, 1 + (n-1)*(c+d) - c]
assert func_1(n, c, d, l) == 'YES'

# End of script