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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `high` is less than `low`, `result` is the index of the first occurrence of the target element in the original `arr` if it exists, otherwise -1, `arr` remains a sorted list of integers, and `target` remains an integer.
    return result
    #The program returns the index of the target element in the sorted list 'arr' if it exists, otherwise -1
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target` as parameters, and returns the index of the first occurrence of `target` in `arr` if it exists, otherwise returns -1. This index corresponds to the position where `target` should be located in the sorted list to maintain sorted order, specifically it is the index of the first occurrence of the target element in the original `arr` if found. If the input list `arr` is empty, the function will return -1. The function does not modify the input list `arr` or the `target` value, preserving their original state. After the function concludes, the state of the program will be: the original list `arr` remains unchanged, the `target` value remains unchanged, and the returned index indicates the position of `target` in `arr` if it exists or -1 if it does not.

