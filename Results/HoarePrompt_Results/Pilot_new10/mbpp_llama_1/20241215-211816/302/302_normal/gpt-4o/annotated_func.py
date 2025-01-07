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
        
    #State of the program after the loop has been executed: `arr` is a sorted list of integers, `target` is an integer, `low` is greater than `high`, if `target` is in `arr`, then `result` is the index of the first occurrence of `target` in `arr`, otherwise `result` is -1
    return result
    #The program returns the index of the first occurrence of `target` in `arr` if `target` is in `arr`, otherwise it returns -1
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `target`, and returns the index of the first occurrence of `target` in `arr` if found, otherwise returns -1, assuming that `arr` is sorted and contains only integer elements

