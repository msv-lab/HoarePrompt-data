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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, indicating that the search has concluded; if the `target` was found in the original `arr`, then `result` is set to the index of the first occurrence of `target`. If the `target` is not present, `result` remains -1. The original `arr` must have been sorted and not empty for the loop to execute.
    return result
    #The program returns the index of the first occurrence of 'target' if found in the sorted 'arr', otherwise it returns -1, indicating that 'target' is not present.
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target`. It performs a binary search to find the index of the first occurrence of `target` in `arr`. If `target` is found, it returns the index of its first occurrence; if `target` is not present, it returns -1. The function assumes that the input list `arr` is sorted and may be empty. If `arr` is empty, it will return -1 since there are no elements to search.

