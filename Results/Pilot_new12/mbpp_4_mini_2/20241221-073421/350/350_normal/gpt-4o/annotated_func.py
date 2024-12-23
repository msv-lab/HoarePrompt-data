#State of the program right berfore the function call: arr is a sorted list of integers and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of integers, `i` is -1 indicating `x` was not found, and `x` is not present in the list `arr`.
    return -1
    #The program returns -1 indicating that x was not found in the sorted list of integers arr.
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `x`. It iterates through the list in reverse order to find the index of the last occurrence of `x`. If `x` is found, the function returns its index. If `x` is not present in the list, the function returns -1. This means the function can return any valid index from 0 to `len(arr) - 1` where `x` is located in `arr`, or -1 if `x` is absent. The function does not account for multiple occurrences of `x`, as it only returns the index of the last occurrence. Edge cases include an empty list, where it correctly returns -1, and a list where `x` is larger than all elements in `arr`, also returning -1.

