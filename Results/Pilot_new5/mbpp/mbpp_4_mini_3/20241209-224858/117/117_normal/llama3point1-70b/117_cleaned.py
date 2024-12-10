def func_1(lst):
    return sum((isinstance(x, int) for x in lst))