#State of the program right berfore the function call: nested_list is a nested list structure.**
def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
        
    #State of the program after the  for loop has been executed: nested_list is a nested list structure, flat_list contains all the elements of nested_list in a flat structure
    return flat_list
    #The program returns a flat_list that contains all the elements of the nested_list in a flat structure
#Overall this is what the function does:The function accepts a parameter nested_list, which is a nested list structure. It recursively flattens the nested list to create a flat_list that contains all the elements of the nested_list in a flat structure. The function handles nested lists of any depth and returns the flat_list.

