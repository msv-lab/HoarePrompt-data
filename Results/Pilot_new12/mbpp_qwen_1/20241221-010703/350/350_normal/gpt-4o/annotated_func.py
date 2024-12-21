#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: - If the loop finds `x`, the function returns the index `i` of the first occurrence of `x` from the end of the list `arr`.
    #- If the loop does not find `x`, the function returns `None`.
    #
    #So, the final output state is:
    #
    #Output State:
    return -1
    #The program returns None
#Overall this is what the function does:This function accepts a list `arr` of integers sorted in non-decreasing order and an integer `x`. It searches for the value `x` in the list `arr` starting from the end of the list. If `x` is found, it returns the index `i` of the first occurrence of `x` from the end of the list. If `x` is not found, it returns `None`. Specifically, the function handles the following cases:
- If `x` is found at index `i`, it returns `i`.
- If no exact match for `x` is found, it checks for the closest match before the last occurrence where `arr[i-1]` is not equal to `x` and `arr[i]` is equal to `x`, returning `i` in this case.
- If no such close match exists, it returns `None`.

Potential edge cases include:
- An empty list `arr` in which case the function should return `None`.
- The list `arr` contains duplicate values of `x`, in which case the function returns the index of the first occurrence of `x` from the end.
- The value `x` is greater than all elements in `arr`, in which case the function should return `None`.

