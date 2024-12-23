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
        
    #State of the program after the  for loop has been executed: `tup` is a tuple, and all elements in `tup` are of type `first_type`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a tuple `tup` as a parameter. It checks whether all elements in the tuple are of the same type as the first element. If the tuple is empty, it returns `True`. If any element in the tuple is of a different type than the first element, it returns `False`. Otherwise, it returns `True`. The function covers all edge cases including an empty tuple and tuples with elements of different types.

