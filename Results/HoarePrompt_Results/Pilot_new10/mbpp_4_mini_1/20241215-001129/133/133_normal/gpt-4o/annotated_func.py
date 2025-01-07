#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length, containing numeric elements.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the element-wise subtraction of corresponding elements in tup1 and tup2
#Overall this is what the function does:The function accepts two tuples, `tup1` and `tup2`, of the same length containing numeric elements, and returns a tuple that consists of the element-wise subtraction of corresponding elements in `tup1` and `tup2`. If the tuples are of different lengths, the function will encounter a `ValueError` during the execution of the `zip` function but this case is not handled within the function.

