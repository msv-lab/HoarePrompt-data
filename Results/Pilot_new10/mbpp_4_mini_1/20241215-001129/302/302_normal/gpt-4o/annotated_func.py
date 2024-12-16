#State of the program right berfore the function call: arr is a list of integers in sorted order, and target is an integer.
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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` is the index of the first occurrence of `target` in `arr` if `target` exists in `arr`; otherwise, `result` remains -1. If `target` is not found, `low` is equal to the position in `arr` where `target` would be if it were inserted while maintaining sorted order.
    return result
    #The program returns the index of the first occurrence of 'target' in 'arr' if 'target' exists; otherwise, it returns -1, and if 'target' is not found, 'low' is equal to the position in 'arr' where 'target' would be inserted while maintaining sorted order.
#Overall this is what the function does:The function accepts a sorted list of integers, `arr`, and an integer `target`. It performs a binary search to find and return the index of the first occurrence of `target` in `arr`. If `target` does not exist in the list, the function returns -1. Additionally, the position where `target` could be inserted to maintain sorted order corresponds to the value of `low` at the end of the search, but this position is not directly returned. Therefore, if `target` is not in the list, the function does not indicate the insertion point and simply returns -1.

