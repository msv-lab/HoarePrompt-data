#State of the program right berfore the function call: nested_list is a list that may contain integers and/or other lists as its elements.
def func_1(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(func_1(i))
        else:
            flat_list.append(i)
        
    #State of the program after the  for loop has been executed: `nested_list` is a list that may be empty, `flat_list` contains all non-list elements from the original `nested_list` plus the results of applying `func_1` to any list elements found in the original `nested_list`, and `i` is the last element of the original `nested_list` if it is not empty, otherwise `i` is undefined.
    return flat_list
    #The program returns `flat_list` which contains all non-list elements from the original `nested_list` plus the results of applying `func_1` to any list elements found in the original `nested_list`.
#Overall this is what the function does:The function accepts a parameter `nested_list`, a list that may contain integers and/or other lists as its elements, and returns a `flat_list` containing all non-list elements from the original `nested_list`. The function recursively flattens the input list, handling nested lists of arbitrary depth. If the input list is empty, the function returns an empty list. The function preserves the original order of elements and does not modify the input list. It handles edge cases such as an input list containing only integers, only lists, or a mix of both, and returns a flat list with all non-list elements. The function does not perform any error checking or handling for non-list inputs, and assumes that the input is a list that may contain integers and/or other lists.

