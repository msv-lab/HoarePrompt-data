#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `num` is an integer, `i` is the index of the last element checked in `arr`, and `x` is the last element checked in `arr`. If `x` equals `num`, the function returns the index `i`. If the loop completes without finding `num`, the function does not return any value. The loop will not execute if `arr` is empty.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_1` takes a sorted list of integers `arr` and an integer `num` as parameters. It searches for the first occurrence of `num` in `arr` and returns the index of `num` if found. If `num` is not found in `arr`, the function returns -1. The function handles the case where `arr` is empty by returning -1, as the loop will not execute and the function will reach the final return statement.

