#State of the program right berfore the function call: nested_list is a list that can contain integers and/or other lists.
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: `nested_list` is a list that can contain integers and/or other lists, `flat_list` contains the flattened version of the original `nested_list`.
    return flat_list
    #The program returns flat_list, which contains the flattened version of the original nested_list that can contain integers and/or other lists
#Overall this is what the function does:The function accepts a nested list that can contain integers and/or other lists as input, processes it recursively to flatten the nested structure, and returns a one-dimensional list containing all the integers from the original nested list. The input list remains unchanged, and the function handles nested lists of arbitrary depth, including the case where the input list is empty or contains only integers. If the input list contains non-integer and non-list elements, the function will include these elements in the output list without modification or error handling, effectively treating them as regular elements. After the function call, the output list will contain all the elements from the original nested list, but in a flattened structure.

