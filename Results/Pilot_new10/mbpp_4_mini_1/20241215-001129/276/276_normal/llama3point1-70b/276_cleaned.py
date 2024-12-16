def func_1(list1, list2, size):
    merged_list = sorted(list1 + list2)
    middle_index = size - 1
    if size % 2 == 0:
        median = (merged_list[middle_index] + merged_list[middle_index + 1]) / 2
    else:
        median = merged_list[middle_index]
    return median