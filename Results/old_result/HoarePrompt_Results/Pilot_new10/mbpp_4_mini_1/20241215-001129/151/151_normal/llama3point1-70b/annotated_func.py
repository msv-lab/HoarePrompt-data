#State of the program right berfore the function call: nested_list is a list that may contain integers or other lists, potentially nested to any depth.
def func_1(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(func_1(i))
        else:
            flat_list.append(i)
        
    #State of the program after the  for loop has been executed: `flat_list` is a flattened version of `nested_list`, containing all integers from `nested_list` and any nested lists within it, with `nested_list` being a list that may contain any number of elements. If `nested_list` is empty, then `flat_list` remains empty.
    return flat_list
    #The program returns the flattened version of `nested_list`, which is `flat_list`, containing all integers from `nested_list` and any nested lists within it. If `nested_list` is empty, then `flat_list` remains empty.
#Overall this is what the function does:The function accepts a list `nested_list`, which can contain integers and/or other lists (nested to any depth). It recursively flattens `nested_list` into a single list containing all integers from the original list and any nested lists within it. If `nested_list` is empty or contains no integers, the function returns an empty list.

