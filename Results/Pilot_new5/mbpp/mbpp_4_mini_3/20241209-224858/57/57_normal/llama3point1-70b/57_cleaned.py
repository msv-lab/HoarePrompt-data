def func_1(list_of_lists):
    return [sorted(sublist, key=str.lower) for sublist in list_of_lists]