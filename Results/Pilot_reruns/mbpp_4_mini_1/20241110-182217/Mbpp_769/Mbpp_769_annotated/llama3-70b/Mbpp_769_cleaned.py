def func_1(list1, list2):
    return sorted(list(set(list1) ^ set(list2)))