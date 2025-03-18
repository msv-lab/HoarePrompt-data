#State of the program right berfore the function call: arr is a sorted list of elements, and target is an element that may be present in arr.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of elements, `target` is an element that may or may not be present in `arr`, and if `target` is found in `arr`, the function returns the index of `target`; otherwise, the function returns `None`, with `i` being `-1` if `target` is not found.
    return -1
    #The program returns -1, indicating that the target element is not found in the sorted list arr
#Overall this is what the function does:The function accepts a sorted list `arr` and a `target` element, then returns the index of the last occurrence of the `target` in `arr` if found, otherwise returns -1, handling the case where the target is not present or the list is empty

