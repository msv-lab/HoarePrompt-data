#State of the program right berfore the function call: tup is a tuple containing elements of any data type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True, indicating a successful execution regardless of the empty tuple `tup`.
    #State of the program after the if block has been executed: *`tup` is a tuple containing elements of any data type, and `tup` is not empty.
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, `first_type` is the type of the first element of `tup`, and all elements in `tup` are of type `first_type`.
    return True
    #The program returns True, indicating that all elements in the non-empty tuple 'tup' are of type 'first_type'.
#Overall this is what the function does:The function accepts a tuple `tup` and returns True if `tup` is empty or if all elements in `tup` are of the same type as the first element. If `tup` contains elements of different types, it returns False.

