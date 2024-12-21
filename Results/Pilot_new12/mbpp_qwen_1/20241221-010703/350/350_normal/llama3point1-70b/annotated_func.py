#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `i` is -1 if the target is not found in the list, otherwise `i` is the index of the first occurrence of the target in the list.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers sorted in non-decreasing order and an integer `target`. It searches the list `arr` from the end to find the index of the first occurrence of `target`. If `target` is found, it returns the index. If `target` is not found, it returns -1.

