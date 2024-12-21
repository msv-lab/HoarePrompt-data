#State of the program right berfore the function call: arr is a sorted list of elements and x is an element that may or may not be present in arr.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of elements, `x` is an element that may or may not be present in `arr`. If `x` is in `arr`, the loop returns the index of the last occurrence of `x`; otherwise, the loop does not return a value (implicitly returning `None`), with `i` being `-1` after the loop finishes.
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a sorted list `arr` and an element `x` as input, and returns the index of the last occurrence of `x` in `arr` if it exists, and -1 otherwise. The function performs a reverse linear search on the input list, checking each element from the last to the first, and returns the index of the first matching element it encounters. If no match is found after checking all elements, the function returns -1, indicating that `x` is not present in `arr`. The input list `arr` remains unmodified throughout the execution of the function. The return value is either a non-negative integer representing the index of the last occurrence of `x`, or -1 if `x` is not found.

