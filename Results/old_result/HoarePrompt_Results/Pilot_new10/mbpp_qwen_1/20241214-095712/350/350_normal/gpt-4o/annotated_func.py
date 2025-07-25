#State of the program right berfore the function call: arr is a list of non-negative integers sorted in non-decreasing order, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of non-negative integers sorted in non-decreasing order, `x` is an integer, `i` is either the index of the first occurrence of `x` in `arr` or -1 if `x` is not found in `arr`.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` of non-negative integers sorted in non-decreasing order and an integer `x`. It iterates over the list in reverse order to find the index of the first occurrence of `x`. If `x` is found, it returns the index of `x`; otherwise, it returns `-1`.

