def func_1(lst):
    return sum((i for i in lst if lst.count(i) == 1))