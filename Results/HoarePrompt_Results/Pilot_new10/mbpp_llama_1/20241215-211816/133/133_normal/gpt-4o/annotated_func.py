#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length, containing elements that support subtraction (e.g., numbers).
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the differences between corresponding elements of `tup1` and `tup2`, where `tup1` and `tup2` are tuples of the same length containing numeric elements.
#Overall this is what the function does:The function accepts two tuples, tup1 and tup2, and returns a tuple containing the differences between corresponding elements of tup1 and tup2. It stops once the end of the shorter tuple is reached if they are not of the same length, and raises a TypeError if the tuples contain non-numeric elements.

