def count_Set_Bits(n):
    return bin(n).count('1')

# Test cases
assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2
