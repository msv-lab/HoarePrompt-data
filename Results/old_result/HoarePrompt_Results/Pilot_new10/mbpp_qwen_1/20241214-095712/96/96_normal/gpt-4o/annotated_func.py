#State of the program right berfore the function call: tup is a tuple containing elements of any type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: tup is a tuple containing elements of any type, and tup is not an empty tuple
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` contains elements of the same type as the first element, and the function returns True if all elements in `tup` are of the type `first_type`, otherwise it returns False.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a tuple `tup` and returns `True` if the tuple is empty or if all elements in the tuple are of the same type as the first element. Otherwise, it returns `False`.

