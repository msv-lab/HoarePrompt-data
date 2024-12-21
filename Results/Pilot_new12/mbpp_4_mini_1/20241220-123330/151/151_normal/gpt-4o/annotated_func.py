#State of the program right berfore the function call: nested_list is a list that may contain integers or other lists, possibly nested to any depth.
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: `flat_list` contains all elements from `nested_list` flattened into a single layer, `nested_list` is a list that may still contain nested structures, and if the loop does not execute, `flat_list` remains an empty list.
    return flat_list
    #The program returns flat_list which contains all elements from nested_list flattened into a single layer, and if the loop does not execute, flat_list remains an empty list.
#Overall this is what the function does:The function `func_1` accepts a parameter `nested_list`, which can contain integers or other lists at any depth. It returns a new list, `flat_list`, which contains all the elements from `nested_list` merged into a single layer, effectively flattening any nested structures. If `nested_list` is empty or contains no elements, the function returns an empty list. The function recursively handles any level of nesting, ensuring that all integers and non-list objects are included in the final output. The original `nested_list` remains unchanged throughout the process.

