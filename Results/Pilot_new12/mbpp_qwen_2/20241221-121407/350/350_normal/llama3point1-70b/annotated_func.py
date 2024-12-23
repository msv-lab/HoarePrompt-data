#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, and the function either returns the index of the first occurrence of `target` in `arr` or returns `-1` if `target` is not found in `arr`.
    return -1
    #-1
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers sorted in non-decreasing order and an integer `target`. It iterates through the list in reverse order to find the first occurrence of `target`. If `target` is found, it returns the index of the first occurrence. If no exact match is found, it returns the second-to-last index of the list `arr`. If the list is empty or `target` is not found and the list has only one element, it returns `-1`.

