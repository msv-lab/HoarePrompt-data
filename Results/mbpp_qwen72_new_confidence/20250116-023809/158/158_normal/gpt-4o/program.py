def set_left_most_unset_bit(n):
    # If all bits are set, return n as it is
    if n & (n + 1) == 0:
        return n
    
    # Find the first unset bit from the left and set it
    position = 1
    while n & position:
        position <<= 1
    
    # Set the found position bit to 1
    return n | position

# Test cases
assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15
