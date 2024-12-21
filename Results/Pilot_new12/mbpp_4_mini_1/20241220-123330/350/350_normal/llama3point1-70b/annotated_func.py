#State of the program right berfore the function call: arr is a sorted list of integers, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of integers that is not empty, `i` is -1, and `target` is not found in `arr`. If `target` were present in `arr`, then `i` would equal the index of `target` in `arr` and the loop would terminate early upon finding the target.
    return -1
    #The program returns -1, indicating that the target is not found in the sorted list 'arr'.
#Overall this is what the function does:The function `func_1` accepts a sorted list of integers `arr` and an integer `target`. It iterates through the list in reverse order to check if the `target` exists in `arr`. If the `target` is found, it returns the index of its last occurrence. If the `target` is not found after checking all elements, the function returns -1. The function does not handle cases where `arr` is empty, which may lead to unexpected behavior or errors. In sum, the function effectively performs a reverse linear search for the target in the sorted list, ensuring it returns the index if found or -1 if not.

