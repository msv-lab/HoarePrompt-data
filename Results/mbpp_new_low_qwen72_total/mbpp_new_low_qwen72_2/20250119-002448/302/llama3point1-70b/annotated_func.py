#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `num` is an integer, and the loop has completed iterating through all elements of `arr`. If `num` was found in `arr`, the function returned the index of `num`. If `num` was not found in `arr`, the function did not return any value (or implicitly returned `None`). The variables `i` and `x` will have the values corresponding to the last element of `arr` if the loop completes without finding `num`.
    return -1
    #The program returns -1, indicating that `num` was not found in the list `arr`.
#Overall this is what the function does:The function `func_1` accepts a sorted list of integers `arr` and an integer `num`. It searches for `num` in `arr` and returns the index of `num` if it is found. If `num` is not found in `arr`, the function returns `-1`. The function does not modify the input list `arr` or the integer `num`. The final state of the program after the function concludes is that either the index of `num` in `arr` is returned, or `-1` is returned if `num` is not present in `arr`.

