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
        
    #State of the program after the loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, `low` is 0, `high` is -1, `result` is -1 if the target is not found, otherwise `result` is the index of `target` in `arr`, `low` and `high` will be such that `low > high`.
    return result
    #The program returns -1 since the target is not found and the initial value of `high` is -1 which means the search range is invalid
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` sorted in non-decreasing order and an integer `target`. It performs a binary search to find the `target` in the list. If the `target` is found, it returns the index of the `target` in the list; otherwise, it returns -1. The function handles the case where the initial value of `high` is -1, indicating that the search range is invalid, by immediately returning -1 without further processing. This ensures that the function correctly indicates that the target is not found when the search range is invalid.

