#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length containing numerical values (integers or floats).
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the differences between the corresponding elements of 'tup1' and 'tup2'
#Overall this is what the function does:The function accepts two parameters, `tup1` and `tup2`, which are tuples of the same length containing numerical values (integers or floats). It returns a new tuple that contains the differences between the corresponding elements of `tup1` and `tup2`. If `tup1` and `tup2` are not of the same length, the function will raise a `ValueError` due to the behavior of the `zip` function. Additionally, if either tuple is empty, the function will return an empty tuple as the output.

