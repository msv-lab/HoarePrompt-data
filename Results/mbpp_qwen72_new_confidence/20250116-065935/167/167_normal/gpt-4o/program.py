def median_numbers(a, b, c):
    # Create a list of the three numbers
    nums = [a, b, c]
    # Sort the list
    nums.sort()
    # Return the middle number as the median
    return float(nums[1])

# Test cases to verify the implementation
assert median_numbers(25, 55, 65) == 55.0
assert median_numbers(20, 10, 30) == 20.0
assert median_numbers(15, 45, 75) == 45.0
