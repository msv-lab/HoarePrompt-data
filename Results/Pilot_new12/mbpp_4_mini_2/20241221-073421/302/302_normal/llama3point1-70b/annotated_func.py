#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer that may or may not be present in arr.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `num` is either present in `arr` or not. If `num` is present, the loop will return the index of `num` in `arr`, and `i` will be equal to the index of the found `num`. If `num` is not present, the loop will complete all iterations, and the return will be None, with `i` being the length of `arr`.
    return -1
    #The program returns -1, indicating that 'num' is not present in the sorted list 'arr'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` sorted in non-decreasing order and an integer `num`. It searches for `num` within `arr`, returning the index of the first occurrence of `num` if it is found. If `num` is not present in `arr`, the function returns -1. The function does not handle edge cases related to empty input lists directly but will naturally return -1 if `arr` is empty, as no iterations will occur. The function also does not explicitly account for duplicate values of `num`, as it will return the index of the first occurrence only.

