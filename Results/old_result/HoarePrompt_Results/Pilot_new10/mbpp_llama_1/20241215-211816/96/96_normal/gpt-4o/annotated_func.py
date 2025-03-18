#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns boolean value True
    #State of the program after the if block has been executed: tup is a tuple, and tup is not empty
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, `first_type` is the type of `tup[0]`, and all elements in `tup` are of type `first_type`, or the function returns False if any element's type differs from `first_type`.
    return True
    #The program returns True, indicating all elements in 'tup' are of the same type as 'tup[0]'
#Overall this is what the function does:The function accepts a tuple and returns True if the tuple is empty or if all its elements are of the same type as the first element, and False otherwise.

