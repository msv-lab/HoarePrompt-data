#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length containing numerical values.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the differences between corresponding elements of tuples tup1 and tup2
#Overall this is what the function does:The function accepts two tuples, `tup1` and `tup2`, of the same length containing numerical values. It returns a tuple containing the differences between corresponding elements of `tup1` and `tup2`. If the tuples are of different lengths, the function will raise a `ValueError` when trying to zip them together.

