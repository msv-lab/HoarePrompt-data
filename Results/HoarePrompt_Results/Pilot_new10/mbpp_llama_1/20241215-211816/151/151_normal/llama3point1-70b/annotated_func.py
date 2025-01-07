#State of the program right berfore the function call: nested_list is a list that can contain integers and/or other lists.
def func_1(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(func_1(i))
        else:
            flat_list.append(i)
        
    #State of the program after the  for loop has been executed: `nested_list` is the original list, `flat_list` contains the flattened elements of `nested_list` where any nested lists are flattened by `func_1`, and `i` is the last element in `nested_list`. If `nested_list` is empty, `flat_list` remains an empty list.
    return flat_list
    #The program returns `flat_list` which contains the flattened elements of the original `nested_list` where any nested lists are flattened by `func_1`. If `nested_list` is empty, the returned `flat_list` remains an empty list.
#Overall this is what the function does:The function accepts a list that can contain integers and/or other lists, and returns a new list with all elements flattened to the top level, handling lists of arbitrary depth and including all types of elements found in the original list.

