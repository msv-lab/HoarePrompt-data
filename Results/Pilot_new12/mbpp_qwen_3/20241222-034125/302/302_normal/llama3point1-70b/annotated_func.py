#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `num` is an integer, and either `i` is the index where `num` is found in `arr` (if `num` is in `arr`), or `i` is the length of `arr` (if `num` is not in `arr`).
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` sorted in non-decreasing order and an integer `num`. It searches for the first occurrence of `num` in `arr`. If `num` is found at the beginning of the list (`i=0`), it returns 0. If `num` is found at the second position (`i=1`), it returns 1. If `num` is found at the third position (`i=2`), it returns 2. If `num` is not found in `arr`, it returns -1.

