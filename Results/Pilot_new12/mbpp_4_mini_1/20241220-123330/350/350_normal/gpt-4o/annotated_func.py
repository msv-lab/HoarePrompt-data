#State of the program right berfore the function call: arr is a sorted list of integers, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of integers, `i` is -1 if `x` is not found in `arr`, and if `x` is present, `i` is the index of the last occurrence of `x` in `arr`. If `x` is not present, the loop will execute `len(arr)` times, and if `len(arr)` is 0, the loop does not execute, leaving `i` undefined.
    return -1
    #The program returns -1, indicating that x is not found in the sorted list of integers 'arr'.
#Overall this is what the function does:The function `func_1` accepts a sorted list of integers `arr` and an integer `x`. It searches for the last occurrence of `x` in `arr`. If found, it returns the index of that last occurrence. If `x` is not present in `arr`, it returns -1. The function handles the case where `arr` is empty by immediately returning -1 without executing the loop. Overall, the function reliably identifies the index of the last occurrence of `x` or indicates its absence.

