#State of the program right berfore the function call: tup is a tuple that may contain elements of any data type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`tup` is a tuple that is not empty and may contain elements of any data type.
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, `first_type` is the type of the first element of `tup`, and all elements in `tup` are of type `first_type` (or the function would have returned False).
    return True
    #The program returns True because the tuple 'tup' is non-empty and all its elements are of the same type as the first element
#Overall this is what the function does:The function accepts a tuple `tup` that may contain elements of any data type. It checks if the tuple is empty; if it is, the function returns True. If `tup` is not empty, the function verifies whether all elements in the tuple are of the same type as the first element. If all elements match this type, the function returns True. However, if any element has a different type, the function returns False. The function does not check for nested non-tuple elements or specific data types beyond matching the type of the first element. In summary, the function ensures that either the tuple is empty or that all its elements are of a uniform type, returning a boolean value based on these conditions.

