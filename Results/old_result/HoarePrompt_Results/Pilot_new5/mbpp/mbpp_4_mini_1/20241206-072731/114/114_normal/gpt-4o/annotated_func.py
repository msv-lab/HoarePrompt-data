#State of the program right berfore the function call: tup is a tuple, and element can be of any data type.
def func_1(tup, element):
    return tup.count(element)
    #The program returns the count of how many times 'element' appears in the tuple 'tup'
#Overall this is what the function does:The function accepts a tuple `tup` and an `element` of any data type, returning the count of how many times `element` appears in `tup`. If `element` is not found, the function returns 0.

