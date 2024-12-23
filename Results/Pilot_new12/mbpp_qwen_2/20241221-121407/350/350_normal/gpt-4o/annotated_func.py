#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `i` is either -1 or the index of the last occurrence of `x` in `arr`, and `i` is -1 if `x` is not found in `arr`.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` sorted in non-decreasing order and an integer `x`. It searches for the last occurrence of `x` in `arr`. If `x` is found, it returns the index of the last occurrence. If `x` is not found, it returns `-1`. The function does this by iterating over the list in reverse order, checking each element against `x`. The final state of the program is that it returns either the index of the last occurrence of `x`, or `-1` if `x` is not found in `arr`.

