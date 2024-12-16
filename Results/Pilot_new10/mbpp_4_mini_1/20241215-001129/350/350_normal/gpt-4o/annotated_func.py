#State of the program right berfore the function call: arr is a list of sorted integers and x is an integer.
def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of sorted integers, `i` is the index of the last element in `arr`, and if `x` is in `arr`, the function returns the index of `x`. If `x` is not in `arr`, the loop iterates through all elements and the function does not return a value.
    return -1
    #The program returns -1, indicating that the value x is not in the list arr of sorted integers.
#Overall this is what the function does:The function accepts a list of sorted integers `arr` and an integer `x`, returning the index of `x` in `arr` if it exists. If `x` is not found, the function returns -1. The function efficiently searches from the end of the list to the beginning and handles cases where `arr` is empty or `x` is not present.

