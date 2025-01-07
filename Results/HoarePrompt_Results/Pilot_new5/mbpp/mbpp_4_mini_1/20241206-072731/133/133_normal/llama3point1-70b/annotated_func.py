#State of the program right berfore the function call: tup1 and tup2 are tuples of the same length, containing numeric elements.
def func_1(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))
    #The program returns a tuple containing the element-wise differences of the numeric elements in tup1 and tup2
#Overall this is what the function does:The function accepts two tuples, `tup1` and `tup2`, of the same length containing numeric elements, and returns a tuple of the element-wise differences between the two tuples. It assumes that both tuples are of equal length and does not handle cases where they are not, which will raise a `ValueError`.

