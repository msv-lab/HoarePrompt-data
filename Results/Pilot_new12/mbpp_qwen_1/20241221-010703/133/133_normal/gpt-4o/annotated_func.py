#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length containing numerical values.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple where each element is the difference between the corresponding elements of tup1 and tup2
#Overall this is what the function does:The function `func_1` accepts two parameters `tup1` and `tup2`, both tuples of the same length containing numerical values, and returns a tuple where each element is the difference between the corresponding elements of `tup1` and `tup2`. The function ensures that both input tuples are of the same length. If the tuples are empty, the function will return an empty tuple. The function does not handle cases where the tuples contain non-numerical values; in such cases, it will raise a TypeError.

