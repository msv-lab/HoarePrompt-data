def replace_list(list1, list2):
    if list1:
        list1[-1:] = list2
    else:
        list1 = list2
    return list1
