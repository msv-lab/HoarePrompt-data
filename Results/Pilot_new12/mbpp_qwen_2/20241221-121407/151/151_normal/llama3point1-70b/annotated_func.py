#State of the program right berfore the function call: nested_list is a list that may contain integers or other lists (nested to any level).
def func_1(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(func_1(i))
        else:
            flat_list.append(i)
        
    #State of the program after the  for loop has been executed: `nested_list` is a list that may contain integers or other lists (nested to any level), `flat_list` is a flattened version of `nested_list` where all elements are at the top level.
    return flat_list
    #`The program returns the flattened version of nested_list stored in flat_list`
#Overall this is what the function does:The function `func_1` takes a parameter `nested_list`, which can be a list containing integers or other nested lists. It recursively flattens the nested list structure into a single-level list called `flat_list`. The function returns this flattened list. This process handles all levels of nesting within the input list. The function does not modify the original `nested_list`; instead, it creates and returns a new list. Potential edge cases include an empty `nested_list`, a `nested_list` that contains no nested lists, or a `nested_list` that contains only integers. The function will handle these cases by simply returning an unmodified `nested_list` if it is already flat or empty.

