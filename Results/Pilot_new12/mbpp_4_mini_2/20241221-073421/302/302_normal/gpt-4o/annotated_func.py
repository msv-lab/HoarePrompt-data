#State of the program right berfore the function call: arr is a sorted list of integers, and target is an integer.
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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` is the index of the `target` in `arr` if found; if `target` was not present, `result` remains -1. The search concludes either with `result` containing the index of the first occurrence of `target` or retains -1, indicating that `target` was not found in the initial sorted list `arr`.
    return result
    #The program returns the index of the target in arr if found, or -1 if the target was not present, since low is greater than high, indicating that the search has concluded.
#Overall this is what the function does:The function `func_1` accepts a sorted list of integers `arr` and an integer `target`. It performs a binary search to find the index of the first occurrence of `target` within `arr`. If `target` is found, the function returns its index; otherwise, it returns -1, indicating that `target` is not present in the list. The function effectively handles edge cases where `arr` is empty or where `target` does not exist in the list. Additionally, it maintains the state of `result` to correctly reflect the index or absence of `target` after the search concludes.

