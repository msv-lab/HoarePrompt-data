#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, and if `target` is found in `arr`, the loop will return the index of the last occurrence of `target`. If `target` is not found, the loop will have executed for all indices of `arr`, and the function will not return any value.
    return -1
    #The program returns -1, indicating that the target integer is not found in the list `arr`.
#Overall this is what the function does:The function accepts a list of integers `arr` sorted in non-decreasing order and an integer `target`. It returns the index of the last occurrence of `target` if found. If `target` is not found, it returns -1. The comments incorrectly suggest returning the second last or third last index under certain conditions, but the actual code does not implement this behavior.

