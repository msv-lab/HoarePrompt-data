#State of the program right berfore the function call: nested_list is a list that can contain integers and/or other lists, which can also be nested.
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: `nested_list` is a list that can contain integers and/or other nested lists, `flat_list` contains the fully flattened elements of `nested_list`.
    return flat_list
    #The program returns flat_list which contains the fully flattened elements of nested_list, where nested_list is a list that can contain integers and/or other nested lists
#Overall this is what the function does:The function accepts a list (`nested_list`) that can contain integers and/or other nested lists, and returns a new list (`flat_list`) containing all the elements of `nested_list` in a fully flattened state, effectively removing any nesting. The original `nested_list` remains unchanged. The function handles recursive nesting of lists, and the returned `flat_list` contains only integers, with all inner lists having been fully flattened. The function does not handle cases where `nested_list` is `None` or not a list, and does not perform any error checking on its input. If `nested_list` contains non-integer and non-list elements, these elements will be included in the `flat_list` without modification. The function's output is a flat list of all the primitive elements (integers and other non-list elements) that were present in the input `nested_list`, in the order they were encountered during the flattening process.

