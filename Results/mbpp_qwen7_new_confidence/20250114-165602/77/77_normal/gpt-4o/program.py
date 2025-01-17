def sum_negativenum(numbers):
    return sum(num for num in numbers if num < 0)

# Test cases
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
assert sum_negativenum([10, 15, -14, 13, -18, 12, -20]) == -52
assert sum_negativenum([19, -65, 57, 39, 152, -639, 121, 44, 90, -190]) == -894
