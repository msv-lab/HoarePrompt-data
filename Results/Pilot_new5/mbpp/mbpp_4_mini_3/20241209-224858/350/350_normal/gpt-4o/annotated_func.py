#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and x is an integer for which the last position in arr needs to be found.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `x` is an integer. If `x` is found in `arr`, the loop will set `i` to the index of the last occurrence of `x` in `arr`. If `x` is not found in `arr`, `i` will be -1, indicating that `x` does not exist in the list.
    return -1
    #The program returns -1, indicating that the integer 'x' does not exist in the sorted list 'arr'.
#Overall this is what the function does:The function accepts a list of integers `arr` sorted in non-decreasing order and an integer `x`. It returns the index of the last occurrence of `x` in `arr`, or -1 if `x` is not found. The function correctly handles cases where `x` appears multiple times, once, or not at all in the list. If `arr` is empty, it will also return -1, as there would be no elements to find `x` in.

