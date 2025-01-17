def left_rotate(n, d):
    # Since we are dealing with 32-bit numbers, we use 32 as the bit width
    BIT_WIDTH = 32
    # Perform the left rotation and ensure it wraps around within the 32-bit boundary
    rotated = ((n << d) | (n >> (BIT_WIDTH - d))) & 0xFFFFFFFF
    return rotated

# Test cases
assert left_rotate(16, 2) == 64
assert left_rotate(10, 2) == 40
assert left_rotate(99, 3) == 792
assert left_rotate(99, 3) == 792
assert left_rotate(0b0001, 3) == 0b1000
assert left_rotate(0b0101, 3) == 0b101000
assert left_rotate(0b11101, 3) == 0b11101000
