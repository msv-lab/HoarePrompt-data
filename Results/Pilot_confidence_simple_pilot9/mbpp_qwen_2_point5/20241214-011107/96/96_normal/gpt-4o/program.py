def check_type(tup):
    if not tup:
        return True  # An empty tuple can be considered as having the same type for all elements.
    
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
    return True

# Test cases
assert check_type((5, 6, 7, 3, 5, 6)) == True
assert check_type((1, 2, "4")) == False
assert check_type((3, 2, 1, 4, 5)) == True
