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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, if the original value of `target` is in `arr` then `result` is the index of the first occurrence of the original value of `target` in `arr`, otherwise `result` is -1, `arr` remains a sorted list of integers, `target` remains an integer
    return result
    #The program returns the index of the first occurrence of the original value of `target` in the sorted list `arr` if `target` is in `arr`, otherwise it returns -1
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target`, and returns the index of the first occurrence of `target` in `arr` if found, otherwise returns -1. The function assumes that the input list `arr` is sorted, and the function does not modify the input list. The function handles edge cases where the target is not in the list, and it also handles cases where the list is empty or contains duplicate elements. If the target is in the list, the function returns the index of the first occurrence of the target, not the last occurrence or any other occurrence. If the list is empty, the function returns -1. The function does not perform any error checking on the input type, so it assumes that the input will always be a list and an integer.

