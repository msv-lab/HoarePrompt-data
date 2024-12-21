#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length containing numerical elements.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the difference of corresponding elements from tuples 'tup1' and 'tup2'
#Overall this is what the function does:The function accepts two tuples, `tup1` and `tup2`, which contain numerical elements of the same length. It returns a new tuple where each element is the result of subtracting the corresponding elements in `tup2` from `tup1`. The function assumes that both input tuples are of the same length; otherwise, it will raise a `ValueError` during the execution of `zip`. If either tuple is empty, the function will return an empty tuple. The output tuple contains the computed differences of the corresponding elements from the input tuples.

