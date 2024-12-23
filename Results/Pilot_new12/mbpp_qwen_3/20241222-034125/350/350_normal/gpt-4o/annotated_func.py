#State of the program right berfore the function call: arr is a list of non-negative integers that is sorted in non-decreasing order, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of non-negative integers sorted in non-decreasing order, `x` is an integer, and `i` is -1 if `x` is not found in `arr`, otherwise `i` is the index of the last occurrence of `x` in `arr`.
    return -1
    #The program returns -1
#Overall this is what the function does:This function searches for the last occurrence of the integer `x` in the sorted list `arr`. If `x` is found in `arr`, the function returns the index of the last occurrence of `x`. If `x` is not found, the function returns `-1`. The function iterates over the list `arr` in reverse order, checking each element against `x`. If a match is found, the function immediately returns the current index. If no match is found after iterating through the entire list, the function returns `-1`. Potential edge cases include when `arr` is empty or contains only one element.

