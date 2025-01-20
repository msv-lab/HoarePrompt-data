#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `num` remains constant throughout the loop, and if `num` is found in `arr`, the function returns the index of the first occurrence of `num` in `arr`. If `num` is not found, the loop completes without returning any value. The final value of `i` is `len(arr) - 1` if the loop completes without finding `num`.
    return -1
    #The program returns -1, indicating that `num` was not found in the list `arr`. The final value of `i` is `len(arr) - 1` if the loop completes without finding `num`.
#Overall this is what the function does:The function `func_1` accepts a sorted list of integers `arr` and an integer `num`. It searches for the first occurrence of `num` in `arr`. If `num` is found, the function returns the index of its first occurrence. If `num` is not found in `arr`, the function returns -1. The function does not modify the input list `arr` or the integer `num`. The final state of the program after the function concludes is that either the index of the first occurrence of `num` in `arr` is returned, or -1 is returned if `num` is not found.

