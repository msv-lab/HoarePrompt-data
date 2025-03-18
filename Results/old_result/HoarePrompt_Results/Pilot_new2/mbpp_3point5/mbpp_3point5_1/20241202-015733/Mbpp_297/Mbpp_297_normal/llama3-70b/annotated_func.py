#State of the program right berfore the function call: nested_list is a list that may contain nested lists.**
def func_1(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(func_1(element))
        else:
            flat_list.append(element)
        
    #State of the program after the  for loop has been executed: `nested_list` is a list with an unknown number of elements, `flat_list` contains a flattened version of `nested_list` after all elements have been processed by the loop.
    return flat_list
    #The program returns a flattened version of `nested_list` after all elements have been processed by the loop
#Overall this is what the function does:The function func_1 accepts a parameter nested_list, which is a list that may contain nested lists. It recursively flattens the nested_list by iterating through each element and appending non-list elements to a flat_list. The function returns the flattened version of nested_list after processing all elements in the list with a loop.

