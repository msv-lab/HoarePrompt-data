def func_1(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
assert func_1([2, 1, 4, 3, 6, 7, 6, 3]) == True
assert func_1([4, 1, 2]) == True
assert func_1([1, 2, 3]) == False