#State of the program right berfore the function call: tup1 and tup2 are tuples of numbers, and for each index i, tup2[i] is not zero.
def func_1(tup1, tup2):
    result = tuple(a // b for a, b in zip(tup1, tup2))
    return result
    #The program returns a tuple `result` where each element is the integer division (`//`) of the corresponding elements from `tup1` and `tup2`. Since `tup2[i]` is guaranteed not to be zero for any index `i`, the division operation is valid for all elements. The length of `result` is the same as the lengths of `tup1` and `tup2`.
#Overall this is what the function does:The function `func_1` accepts two tuples `tup1` and `tup2` of numbers, where each element in `tup2` is guaranteed to be non-zero. It returns a new tuple `result` where each element is the integer division (`//`) of the corresponding elements from `tup1` and `tup2`. The length of the returned tuple `result` is the same as the lengths of `tup1` and `tup2`. If the lengths of `tup1` and `tup2` are not equal, a `ValueError` will be raised due to the `zip` function, which stops when the shortest input iterable is exhausted.

