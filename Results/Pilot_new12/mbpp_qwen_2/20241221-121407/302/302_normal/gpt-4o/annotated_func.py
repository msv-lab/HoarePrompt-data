#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
    #State of the program after the loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, `low` and `high` are integers such that `low` must be less than or equal to `high`, `result` is the index of the target in `arr` if found, otherwise -1, `mid` is an integer. If the target is found, `result` is set to the appropriate index; if not found, `result` remains -1. After all iterations, `low` will be greater than `high`.
    return result
    #`The program returns -1` since the target is not found in the list and the condition low > high is met
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers sorted in non-decreasing order and an integer `target`. It performs a binary search to find the `target` within the list. If the `target` is found, it sets the `result` to the index of the `target` in `arr` and returns this index. If the `target` is not found and the condition `low > high` is met, the function returns `-1`. The final state of the program after the function concludes is that the variable `result` holds either the index of the `target` if it was found, or `-1` if the `target` was not found.

