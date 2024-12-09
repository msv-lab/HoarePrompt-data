#State of the program right berfore the function call: tup is a tuple containing elements of any type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`tup` is a tuple containing elements of any type, and `tup` is not empty.
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a tuple containing elements of the same type, `first_type` is the type of the elements in `tup`, and all elements in `tup` are of type `first_type`.
    return True
    #The program returns True, indicating a successful execution without any conditions affecting the outcome
#Overall this is what the function does:The function accepts a tuple `tup` and checks if all the elements within it are of the same type. It returns `True` if the tuple is empty or if all elements are of the same type; otherwise, it returns `False`. The function does not handle the case where the tuple contains elements of different types adequately, as it only checks the first element's type against all others without any additional conditions for tuples of length 1 or empty tuples.

