#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length, and each element in tup2 is non-zero.
def func_1(tup1, tup2):
    result = tuple(a // b for a, b in zip(tup1, tup2))
    return result
    #The program returns a tuple `result` where each element is the floor division of the corresponding elements from `tup1` and `tup2`. Each element in `tup2` is non-zero, ensuring no division by zero errors.
#Overall this is what the function does:The function `func_1` accepts two tuples, `tup1` and `tup2`, both of which are expected to be of the same length, and each element in `tup2` is non-zero. It returns a new tuple `result` where each element is the floor division (integer division) of the corresponding elements from `tup1` and `tup2`. The function ensures that no division by zero occurs due to the non-zero constraint on `tup2`. If the input tuples are not of the same length or if `tup2` contains a zero, the behavior is undefined and may result in an error.

