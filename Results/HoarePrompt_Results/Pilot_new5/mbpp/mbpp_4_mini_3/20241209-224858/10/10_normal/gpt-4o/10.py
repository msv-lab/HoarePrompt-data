def find_Volume(base, height, length):
    base_area = 0.5 * base * height
    volume = base_area * length
    return volume

# Tests
assert find_Volume(10, 8, 6) == 240
assert find_Volume(3, 2, 2) == 6
assert find_Volume(1, 2, 1) == 1
