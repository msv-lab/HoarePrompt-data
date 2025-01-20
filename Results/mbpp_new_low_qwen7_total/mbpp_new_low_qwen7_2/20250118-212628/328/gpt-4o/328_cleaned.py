def func_1(n):
    count = 0
    number = 1
    while count < n:
        if number & number - 1 != 0:
            count += 1
        number += 1
    return number - 1
assert func_1(7) == 11
assert func_1(4) == 7
assert func_1(9) == 13