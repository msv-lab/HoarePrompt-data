#State of the program right berfore the function call: tup is a tuple containing elements of any data type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`tup` is a tuple containing elements of any data type, and `tup` is not empty.
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a tuple containing elements of the same data type, `first_type` is the type of the elements in `tup`, and all elements in `tup` are of type `first_type`.
    return True
    #The program returns True, indicating that the execution of the code is successful regardless of the elements in the tuple `tup`
#Overall this is what the function does:The function accepts a tuple `tup` and returns `True` if the tuple is empty or if all elements in the tuple are of the same data type; otherwise, it returns `False`.

