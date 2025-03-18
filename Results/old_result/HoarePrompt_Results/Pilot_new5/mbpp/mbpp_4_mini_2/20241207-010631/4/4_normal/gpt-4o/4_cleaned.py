def func_1(a, b):
    xor_result = a ^ b
    return xor_result != 0 and xor_result & xor_result - 1 == 0
assert func_1(13, 9) == True
assert func_1(15, 8) == False
assert func_1(2, 4) == False
assert func_1(2, 3) == True
assert func_1(5, 1) == True
assert func_1(1, 5) == True