def func_1(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)