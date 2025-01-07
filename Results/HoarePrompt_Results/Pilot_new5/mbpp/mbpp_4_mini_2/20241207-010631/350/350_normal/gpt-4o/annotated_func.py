#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `i` is -1, and if `x` is not found in `arr`, the loop has finished executing without returning any value.
    return -1
    #The program returns -1, indicating that the value x is not found in the list 'arr'
#Overall this is what the function does:The function accepts a list of integers `arr` sorted in non-decreasing order and an integer `x`. It searches for the last occurrence of `x` in the list and returns its index. If `x` is not found in the list, it returns -1.

