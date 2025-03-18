#State of the program right berfore the function call: arr is a sorted list of elements, and x is an element that may or may not be present in arr.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of elements, `x` is an element that may or may not be present in `arr`. If `x` is found in `arr`, the function returns its index; otherwise, the loop completes with `i` being `-1`, indicating `x` was not found. If `arr` is empty, the loop does not execute.
    return -1
    #The program returns -1, indicating that the element `x` was not found in the sorted list `arr`, or the list `arr` is empty.
#Overall this is what the function does:The function accepts a sorted list `arr` and an element `x`, and returns the index of `x` if it is found in `arr` while iterating from the end towards the beginning; otherwise, it returns -1, indicating that `x` was not found in `arr` or `arr` is empty.

