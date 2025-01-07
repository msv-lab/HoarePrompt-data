def func_1(lst):
    return all((lst[i] <= lst[i + 1] for i in range(len(lst) - 1)))