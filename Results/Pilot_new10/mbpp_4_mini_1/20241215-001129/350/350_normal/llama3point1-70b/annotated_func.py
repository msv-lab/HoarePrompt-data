#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, and if `target` is found, the function would have returned the index of the target in `arr`; otherwise, the loop completes without finding the target, and no value is returned. If the loop does not execute, `arr` can be empty, and `target` remains the initial integer.
    return -1
    #The program returns -1 indicating that the target integer is not found in the sorted list of integers `arr`
#Overall this is what the function does:The function accepts a list of integers `arr`, which is expected to be sorted in non-decreasing order, and an integer `target`. It searches for the last occurrence of `target` in `arr` and returns its index. If `target` is not found, the function returns -1. The function does not handle any exceptions or edge cases where `arr` might be empty.

