#State of the program right berfore the function call: nested_list is a list that may contain integers or other lists, which can be nested to any level.
def func_1(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(func_1(i))
        else:
            flat_list.append(i)
        
    #State of the program after the  for loop has been executed: `flat_list` contains all integers from `nested_list` and all elements returned from `func_1` applied to any sub-lists within `nested_list`. If `nested_list` is empty, `flat_list` is also empty.
    return flat_list
    #The program returns flat_list, which contains all integers from nested_list and all elements returned from func_1 applied to any sub-lists within nested_list. If nested_list is empty, flat_list is also empty.
#Overall this is what the function does:The function accepts a list `nested_list` which may contain integers or other lists (including nested lists). It returns a flat list containing all integers extracted from `nested_list` and any nested lists within it. If `nested_list` is empty, it will return an empty list.

