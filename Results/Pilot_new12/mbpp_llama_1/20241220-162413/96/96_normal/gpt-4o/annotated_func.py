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
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, `first_type` is the type of `tup[0]`, and either the function has returned `False` (indicating a type mismatch) or all elements in `tup` are of type `first_type` and `element` is the last element of `tup`.
    return True
    #The program returns True, indicating that all elements in `tup` are of type `first_type`, where `first_type` is the type of `tup[0]` and `tup` is a non-empty tuple
#Overall this is what the function does:The function `func_1` checks if all elements in the input tuple `tup` are of the same type as the first element in `tup`. If `tup` is empty, it returns `True`. If all elements in `tup` are of the same type, it returns `True`. Otherwise, it returns `False`. The function handles potential edge cases such as an empty tuple, a tuple with a single element, and a tuple with multiple elements of different types. After executing the function, the state of the program will be one of two possible outcomes: the function will have returned `True` if the tuple is empty or all elements are of the same type, or it will have returned `False` if the tuple contains elements of different types. The function does not modify the input tuple `tup` in any way, it only checks its contents and returns a boolean value indicating whether all elements are of the same type.

