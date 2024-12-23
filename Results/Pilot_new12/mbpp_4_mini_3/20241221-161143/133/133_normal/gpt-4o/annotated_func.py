#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length, containing numerical elements.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the difference of corresponding elements from tup1 and tup2
#Overall this is what the function does:The function accepts two tuples, `tup1` and `tup2`, which must be of the same length and contain numerical elements. It returns a tuple that contains the differences of the corresponding elements of `tup1` and `tup2`. The function will raise a `ValueError` if the two tuples are not of the same length, as this is a necessary requirement for the computation. If either tuple is empty, the function will return an empty tuple.

