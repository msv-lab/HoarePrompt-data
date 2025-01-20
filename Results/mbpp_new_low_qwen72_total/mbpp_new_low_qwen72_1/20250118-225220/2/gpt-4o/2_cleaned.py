def func_1(n):
    if n <= 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False
assert func_1(1) == True
assert func_1(2) == False
assert func_1(10) == True
assert func_1(35) == True
assert func_1(37) == False