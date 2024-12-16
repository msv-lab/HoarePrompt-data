def func_1(lst):
    if not lst:
        return False
    lst_sorted = sorted(lst)
    for i in range(len(lst_sorted) - 1):
        if lst_sorted[i + 1] - lst_sorted[i] != 1:
            return False
    return True
assert func_1([1, 2, 3, 4, 5]) == True
assert func_1([1, 2, 3, 5, 6]) == False
assert func_1([1, 2, 1]) == False