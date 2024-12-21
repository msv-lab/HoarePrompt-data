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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` is the index of the first occurrence of `target` in `arr` if `target` exists, otherwise `result` remains -1. If `target` was present in the array, original `low` must have been less than or equal to the original `high`, and the loop executes until `low` exceeds `high`. If `target` is not found, `result` remains -1 indicating the absence of `target`.
    return result
    #The program returns -1 indicating that the target was not found in the array, as low is greater than high.
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target`. It performs a binary search to find the index of the first occurrence of `target` in `arr`. If `target` exists in the array, it returns the index of its first occurrence; otherwise, it returns -1 to indicate that the target was not found. The implementation correctly handles cases where the target is less than, greater than, or equal to elements in the array, and it ensures that it searches for the first occurrence by continuing to search in the left half of the array when a match is found. There are no considerations for empty arrays or non-integer elements, which could be potential edge cases, but within the scope of a sorted list of integers, the behavior is well-defined.

