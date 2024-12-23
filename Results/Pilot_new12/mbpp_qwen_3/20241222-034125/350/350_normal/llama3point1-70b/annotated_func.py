#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, and `i` is either the index of the last occurrence of `target` in `arr` or `None` if `target` is not found in `arr`.
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` sorted in non-decreasing order and an integer `target`. It iterates through the list in reverse order to find the last occurrence of `target`. If `target` is found, it returns the index of the last occurrence. If `target` is not found, it returns `-1`. The possible return values are:
- `len(arr) - 1`: If `target` is the last element in the list.
- `-1`: If `target` is not found in the list.

There are no other specific indices like `len(arr) - 2` or `len(arr) - 3` mentioned in the code or annotations, and these should be considered as incorrect or redundant information. The function only returns the index of the last occurrence of `target` or `-1` if `target` is not found.

