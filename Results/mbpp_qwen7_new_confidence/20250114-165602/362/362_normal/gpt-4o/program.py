def first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None  # In case there is no odd number in the list

# Test cases
assert first_odd([1, 3, 5]) == 1
assert first_odd([2, 4, 1, 3]) == 1
assert first_odd([8, 9, 1]) == 9
