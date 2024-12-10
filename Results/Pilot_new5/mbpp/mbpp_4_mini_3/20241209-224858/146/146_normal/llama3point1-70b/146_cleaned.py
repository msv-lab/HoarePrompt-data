def func_1(list_of_lists):
    max_len = max((len(sublist) for sublist in list_of_lists))
    max_sublists = [sublist for sublist in list_of_lists if len(sublist) == max_len]
    return (max_len, max_sublists[0])