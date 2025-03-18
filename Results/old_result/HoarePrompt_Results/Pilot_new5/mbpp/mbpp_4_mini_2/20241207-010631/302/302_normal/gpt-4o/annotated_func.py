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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` is the index of the last occurrence of `target` in `arr` if `target` exists in `arr`, or -1 if `target` does not exist in `arr`. If `target` is greater than the largest element in `arr`, then `low` will have become `len(arr)`, and `high` will be less than `len(arr) - 1`. If `target` is less than the smallest element in `arr`, then `low` will still be 0 and `high` will be -1 indicating that `target` is not present. If `target` is found, `result` will hold the index of its last occurrence.
    return result
    #The program returns the index of the last occurrence of `target` in `arr` if `target` exists in `arr`, or -1 if `target` does not exist in `arr`.
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target`, returning the index of the last occurrence of `target` in `arr` if `target` exists; otherwise, it returns -1 if `target` does not exist in `arr`. The function correctly handles cases where `target` is less than the smallest element or greater than the largest element in `arr`.

