#State of the program right berfore the function call: tup is a tuple containing elements of any data type.
def func_1(tup):
    return len(set(type(x) for x in tup)) == 1
    #The program returns True if all elements in the tuple 'tup' are of the same data type, otherwise it returns False.
#Overall this is what the function does:The function accepts a tuple `tup` and returns `True` if all elements in the tuple are of the same data type; otherwise, it returns `False`. It does not handle empty tuples specifically, but an empty tuple will also return `True` since there are no differing types present.

