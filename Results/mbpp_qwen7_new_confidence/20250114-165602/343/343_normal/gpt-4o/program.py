def tuple_str_int(s: str) -> tuple:
    # Remove the parentheses and split the string by commas
    elements = s.strip('()').split(',')
    # Convert each element to an integer and return as a tuple
    return tuple(int(e) for e in elements)

# Test cases to validate the solution
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)
