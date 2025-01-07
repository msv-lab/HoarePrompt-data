#State of the program right berfore the function call: nested_list is a nested list structure.**
def func_1(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(func_1(element))
        else:
            flat_list.append(element)
        
    #State of the program after the  for loop has been executed: nested_list is a nested list structure with no more elements left to be processed. flat_list contains all the elements from the nested_list after applying func_1 to any nested lists.
    return flat_list
    #The program returns flat_list which contains all the elements from the nested_list after applying func_1 to any nested lists
#Overall this is what the function does:The function func_1 accepts a parameter nested_list, which is a nested list structure, and recursively flattens the nested list by applying func_1 to any inner lists. It returns a flat_list containing all the elements from the nested_list after flattening.

