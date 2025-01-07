#State of the program right berfore the function call: tup is a tuple and element is a value to be searched in the tuple.**
def func_1(tup, element):
    return tup.count(element)
    #The program returns the number of occurrences of the value 'element' in the tuple 'tup'
#Overall this is what the function does:The function `func_1` takes two parameters, a tuple `tup`, and a value `element`, then it returns the number of occurrences of `element` in the tuple `tup`. If `element` is not found in `tup`, the function will return 0. The function effectively counts the occurrences of a specific value within a tuple.

