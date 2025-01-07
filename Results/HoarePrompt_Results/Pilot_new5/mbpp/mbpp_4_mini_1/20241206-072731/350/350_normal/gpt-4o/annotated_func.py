#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order; if `x` is in `arr`, the loop will return the index of the last occurrence of `x`, otherwise the loop will have executed for all elements in `arr` without finding `x`. If `x` is not found, `i` will be -1 after the loop completes.
    return -1
    #The program returns -1, indicating that the value `x` is not found in the list `arr`, as `i` will be -1 after the loop completes.
#Overall this is what the function does:The function accepts a list of integers `arr` sorted in non-decreasing order and an integer `x`. It returns the index of the last occurrence of `x` in `arr` if `x` is found; otherwise, it returns -1 if `x` is not present in the list.

