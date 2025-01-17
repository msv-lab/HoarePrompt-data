from itertools import combinations
from functools import reduce
from operator import mul

def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    # Generate all sublists of all lengths
    for length in range(1, len(lst) + 1):
        for sublist in combinations(lst, length):
            # Compute the product of the sublist
            product = reduce(mul, sublist)
            # Add the product to the total sum
            total_sum += product
    return total_sum

# Test cases
assert sum_Of_Subarray_Prod([1,2,3]) == 20
assert sum_Of_Subarray_Prod([1,2]) == 5
assert sum_Of_Subarray_Prod([1,2,3,4]) == 84
