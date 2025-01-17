def is_product_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False

# Test cases
assert is_product_even([1, 2, 3])
assert is_product_even([1, 2, 1, 4])
assert not is_product_even([1, 1])
