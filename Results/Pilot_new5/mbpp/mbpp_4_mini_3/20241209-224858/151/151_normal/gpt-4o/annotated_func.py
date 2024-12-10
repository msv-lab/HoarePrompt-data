#State of the program right berfore the function call: nested_list can be a list containing integers and/or other lists, potentially nested to multiple levels.
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: `flat_list` contains all integers from `nested_list` and its nested lists in a flattened form; `nested_list` is a list that can contain integers and/or other lists. If `nested_list` is empty, `flat_list` remains empty.
    return flat_list
    #The program returns flat_list, which contains all integers from nested_list and its nested lists in a flattened form; if nested_list is empty, flat_list remains empty.
#Overall this is what the function does:The function accepts a list called `nested_list`, which may contain integers and/or other nested lists. It recursively flattens the structure, returning a single list (`flat_list`) that contains all integers extracted from `nested_list` and its nested lists. If `nested_list` is empty or contains no integers, the function returns an empty list.

