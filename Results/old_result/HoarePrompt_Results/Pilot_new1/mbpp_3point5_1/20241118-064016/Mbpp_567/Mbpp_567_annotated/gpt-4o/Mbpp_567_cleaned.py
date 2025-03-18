def func_1(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
assert func_1([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) == True
assert func_1([1, 2, 4, 6, 8, 10, 12, 14, 20, 17]) == False
assert func_1([1, 2, 4, 6, 8, 10, 15, 14, 20]) == False