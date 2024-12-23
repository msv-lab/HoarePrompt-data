#State of the program right berfore the function call: arr is a list of sorted integers, and target is an integer that may or may not be present in arr.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of sorted integers, `i` is -1 indicating that the loop has completed without finding `target`, and the function does not return a value if `target` is not found in `arr`.
    return -1
    #The program returns -1 indicating that the target was not found in the list of sorted integers `arr`, and `i` is -1 which signifies that the loop completed without finding the target.
#Overall this is what the function does:The function `func_1` accepts a list of sorted integers `arr` and an integer `target`. It searches for the last occurrence of `target` in `arr` and returns its index. If `target` is found, the function returns the index of the last occurrence; if not found, it returns -1. Importantly, the function does not handle cases for when the input list `arr` is empty, which would lead to an index error or undefined behavior. Besides, the return postconditions suggest incorrect behavior since if the last element isn't equal to `target`, no specific index should be returned other than -1. Thus, the function's output is either the last index of `target` found or -1 if not present.

