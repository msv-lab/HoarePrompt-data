#State of the program right berfore the function call: tup is a tuple containing elements of varying data types.
def func_1(tup):
    return len(set(type(x) for x in tup)) == 1
    #The program returns True if all elements in the tuple 'tup' are of the same data type, and False otherwise.
#Overall this is what the function does:The function accepts a tuple `tup` and returns `True` if all elements in the tuple are of the same data type. If the tuple contains elements of varying data types, it returns `False`. The function does not handle the case where the tuple is empty, but logically should return `True` since there are no differing types.

