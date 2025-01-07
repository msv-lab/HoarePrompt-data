#State of the program right berfore the function call: nested_list is a list that may contain integers, other lists, or a combination of both, and can be nested to any level.
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: `flat_list` is a flattened version of `nested_list`, which may contain integers or other lists, or a combination of both. The length of `flat_list` depends on the total number of non-list elements and the elements returned by `func_1` applied to any sublists. `nested_list` is unchanged from its initial state. If `nested_list` is empty, `flat_list` will also be an empty list.
    return flat_list
    #The program returns a flattened version of `nested_list`, which may contain integers or other lists, or a combination of both, depending on the total number of non-list elements and the elements returned by `func_1` applied to any sublists. If `nested_list` is empty, `flat_list` will also be an empty list.
#Overall this is what the function does:The function accepts a potentially nested list `nested_list`, which can contain integers, other lists, or a combination of both. It returns a flattened list containing all non-list elements from `nested_list`. If `nested_list` is empty, it returns an empty list. The function correctly handles any level of nesting and does not alter the original `nested_list`.

