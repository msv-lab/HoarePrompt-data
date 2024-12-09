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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, indicating that the search has concluded; `result` is the index of the first occurrence of `target` in `arr` if `target` exists in the array, otherwise `result` remains -1. The value of `arr` remains unchanged, and `target` is an integer.
    return result
    #The program returns the index of the first occurrence of `target` in `arr` if `target` exists, otherwise -1, as `result` remains unchanged based on the search conclusion indicated by `low` being greater than `high`.
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target`. It performs a binary search to find the index of the first occurrence of `target` in `arr`. If `target` exists, it returns its index; if not, it returns -1. The function correctly handles edge cases, including an empty list where it will return -1 since `target` cannot be found in an empty array.

