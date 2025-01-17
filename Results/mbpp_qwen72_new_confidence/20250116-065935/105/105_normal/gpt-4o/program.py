def even_bit_set_number(n):
    # Iterate through the bits and set the even bits
    even_pos = 0
    while (1 << even_pos) <= n:
        n |= (1 << even_pos)
        even_pos += 2
    return n

# Tests
assert even_bit_set_number(10) == 10
assert even_bit_set_number(20) == 30
assert even_bit_set_number(30) == 30
