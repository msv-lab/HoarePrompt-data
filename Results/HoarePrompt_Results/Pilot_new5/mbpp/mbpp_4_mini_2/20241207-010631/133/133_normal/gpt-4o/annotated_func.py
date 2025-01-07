#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length containing numerical values.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the differences between corresponding elements of `tup1` and `tup2`
#Overall this is what the function does:The function accepts two tuples, `tup1` and `tup2`, and returns a tuple containing the differences between corresponding elements of `tup1` and `tup2`. It assumes both tuples are of the same length and contain numerical values. If the tuples have different lengths, the behavior is undefined since `zip` will stop at the shortest tuple.

