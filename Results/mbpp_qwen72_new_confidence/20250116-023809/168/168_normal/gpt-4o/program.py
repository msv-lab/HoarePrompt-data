def sum_of_digits(lst):
    def digit_sum(n):
        n = abs(n)  # Ensure n is positive
        return sum(int(digit) for digit in str(n))
    
    total_sum = 0
    for item in lst:
        if isinstance(item, int):  # Check if item is an integer
            total_sum += digit_sum(item)
    
    return total_sum

# Test cases
assert sum_of_digits([10, 2, 56]) == 14
assert sum_of_digits([10, 20, 4, 5, 'b', 70, 'a']) == 19
assert sum_of_digits([10, 20, -4, 5, -70]) == 19
