#State of the program right berfore the function call: nested_list is a list that may contain integers or other lists (nested to any level).
def func_1(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(func_1(i))
        else:
            flat_list.append(i)
        
    #State of the program after the  for loop has been executed: `nested_list` is a list that may contain integers or other lists (nested to any level), `flat_list` is the fully flattened version of `nested_list` obtained by recursively extending `flat_list` with each element in `nested_list` until no more elements are lists.
    return flat_list
    #The program returns `flat_list`, which is the fully flattened version of `nested_list` obtained by recursively extending `flat_list` with each element in `nested_list` until no more elements are lists
#Overall this is what the function does:The function `func_1` accepts a list `nested_list` and returns a fully flattened list `flat_list` by recursively processing and flattening any nested lists within `nested_list`.

