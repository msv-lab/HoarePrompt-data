#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `num` is an integer, and `i` is either the index of the first occurrence of `num` in `arr` or `len(arr)`, and `x` is the element in `arr` at index `i` (if `i < len(arr)`), and the function returns `i` if `x == num`, otherwise it returns `None`.
    return -1
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` (sorted in non-decreasing order) and an integer `num`, and returns the index of the first occurrence of `num` in `arr` or `-1` if `num` is not found.

