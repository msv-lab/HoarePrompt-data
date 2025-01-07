#State of the program right berfore the function call: arr is a list of sorted integers, and target is an integer.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of sorted integers, `target` is an integer, and if `target` is not found in `arr`, the loop will have executed `len(arr)` times. If `target` is found, the loop will return the index of the last occurrence of `target` in `arr` (if duplicates exist), otherwise, the output index will be None, and `i` will be -1 after all iterations.
    return -1
    #The program returns -1, indicating that the target is not found in the list 'arr', and the loop has executed len(arr) times, resulting in index 'i' being -1 after all iterations.
#Overall this is what the function does:The function accepts a list of sorted integers `arr` and an integer `target`, and returns the index of the last occurrence of `target` in `arr` if found; otherwise, it returns -1 if `target` is not present in the list. The function handles the case of duplicates by returning the index of the last occurrence and uses a reverse iteration through `arr` to find the target.

