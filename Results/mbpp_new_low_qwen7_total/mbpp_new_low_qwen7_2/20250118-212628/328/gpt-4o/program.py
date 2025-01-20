def is_polite(n):
    count = 0
    number = 1
    while count < n:
        if (number & (number - 1)) != 0:  # Check if number is not a power of 2
            count += 1
        number += 1
    return number - 1

# Testing the function
assert is_polite(7) == 11
assert is_polite(4) == 7
assert is_polite(9) == 13
