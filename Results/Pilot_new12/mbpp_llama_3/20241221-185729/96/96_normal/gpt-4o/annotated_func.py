#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: tup is a tuple, and tup is not empty
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, `first_type` is the type of the first element of `tup`, and either all elements in `tup` are of type `first_type` (if the loop completes normally) or the function returns `False` as soon as an element of a different type is encountered.
    return True
    #The program returns True, indicating that all elements in the tuple 'tup' are of the same type, which is 'first_type'
#Overall this is what the function does:The function accepts a tuple parameter `tup` and returns a boolean value indicating whether all elements in `tup` are of the same type. If `tup` is empty, it returns `True`. If all elements in `tup` are of the same type, it returns `True`; otherwise, it returns `False` as soon as it encounters an element of a different type. The function handles potential edge cases such as an empty tuple and tuples with elements of different types. The final state of the program after execution will be one of two possible return values: `True` if the tuple is empty or all elements are of the same type, and `False` if the tuple is non-empty and contains elements of different types.

