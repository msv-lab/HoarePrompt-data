#State of the program right berfore the function call: nested_list is a list that may contain nested lists.**
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: `flat_list` is a list. If `item` is a list, `flat_list` will contain elements returned by `func_1(item)` for every element in `nested_list` that is a list. `nested_list` is a list.
    return flat_list
    #The program returns flat_list which is a list containing elements returned by func_1(item) for every element in nested_list that is a list
#Overall this is what the function does:The function func_1 accepts a list `nested_list` that may contain nested lists. It recursively flattens the nested structure and returns a flat list containing all elements from the nested_list.

