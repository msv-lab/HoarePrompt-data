#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length containing numerical values.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple where each element is the result of subtracting the corresponding element of tup2 from tup1
#Overall this is what the function does:The function `func_1` accepts two tuples `tup1` and `tup2` of the same length, and returns a new tuple where each element is the result of subtracting the corresponding element of `tup2` from `tup1`.

