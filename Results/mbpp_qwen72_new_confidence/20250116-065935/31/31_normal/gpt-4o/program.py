def dif_Square(n):
    # A number can be represented as the difference of two squares if
    # and only if it is not of the form 4k + 2.
    return n % 4 != 2

# Tests
assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True
