#State of the program right berfore the function call: nested_list is a nested list structure.**
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: nested_list is a nested list structure with any number of elements. If an item is a list, flat_list will contain all the elements returned by func_1(item) for all nested lists in nested_list. If an item is not a list, flat_list will contain all the elements from nested_list in the order they appeared.
    return flat_list
    #The program returns flat_list which contains all the elements returned by func_1(item) for all nested lists in nested_list, and if an item is not a list, flat_list will contain all the elements from nested_list in the order they appeared
#Overall this is what the function does:The function func_1 accepts a nested list structure as a parameter and recursively flattens it into a single list by extracting all elements from nested lists. The flat_list returned contains all elements in the order they appeared in the original nested list.

