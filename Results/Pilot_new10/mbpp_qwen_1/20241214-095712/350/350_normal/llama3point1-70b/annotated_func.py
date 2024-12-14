#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: Output State: `i` is the index of the first occurrence of `target` in `arr` if `target` is present in `arr`; otherwise, `i` is -1, `arr` is a non-empty list of integers sorted in non-decreasing order, and `target` is an integer.
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list `arr` of integers sorted in non-decreasing order and an integer `target`, and returns the index of the first occurrence of `target` if it is found; otherwise, it returns -1.

