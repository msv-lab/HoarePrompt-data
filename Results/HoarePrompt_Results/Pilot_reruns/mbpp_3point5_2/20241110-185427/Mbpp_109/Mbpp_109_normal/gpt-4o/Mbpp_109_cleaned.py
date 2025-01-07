def func_1(binary_str, num_rotations):
    count = 0
    for _ in range(num_rotations):
        binary_str = binary_str[-1] + binary_str[:-1]
        integer_value = int(binary_str, 2)
        if integer_value % 2 == 1:
            count += 1
    return count
assert func_1('011001', 6) == 3
assert func_1('11011', 5) == 4
assert func_1('1010', 4) == 2