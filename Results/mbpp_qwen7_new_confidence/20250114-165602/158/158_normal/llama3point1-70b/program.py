def set_left_most_unset_bit(n):
    # Find the left most unset bit
    i = 0
    while (n & (1 << i)) != 0:
        i += 1

    # Set the left most unset bit
    return n | (1 << i)
