#State of the program right berfore the function call: tup is a tuple and element is any type of object that can be compared with the elements in the tuple.
def func_1(tup, element):
    return tup.count(element)
    #The program returns the number of occurrences of 'element' in tuple 'tup'
#Overall this is what the function does:The function accepts a tuple `tup` and an `element`, and returns the number of occurrences of `element` in `tup`. If `tup` is not a tuple, it raises an AttributeError. If `element` is not a comparable object, it raises a TypeError. If `tup` is an empty tuple or `element` is not found in `tup`, it returns 0.

