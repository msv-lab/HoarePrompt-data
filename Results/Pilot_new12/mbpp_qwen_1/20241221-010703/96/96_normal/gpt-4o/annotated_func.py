#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: tup is a tuple, and tup is not an empty tuple
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, and all elements in `tup` have the same type as `first_type`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a tuple `tup` as a parameter. It checks whether `tup` is an empty tuple or not. If `tup` is empty, it returns `True`. Otherwise, it proceeds to check if all elements in `tup` are of the same type as the first element. If any element in `tup` is of a different type, it returns `False`. If all elements are of the same type, it returns `True`. Therefore, the function returns `True` if `tup` is either empty or all elements are of the same type, and `False` otherwise.

