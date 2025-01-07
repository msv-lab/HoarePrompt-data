def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return (True, index)
    return (False, -1)
assert func_1([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31) == (True, 3)
assert func_1([12, 32, 45, 62, 35, 47, 44, 61], 61) == (True, 7)
assert func_1([9, 10, 17, 19, 22, 39, 48, 56], 48) == (True, 6)