#State of the program right berfore the function call: arr is a sorted list of integers, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of integers, `i` is the index of the first occurrence of `num` in `arr` or indicates that `num` is not in `arr`, and if `num` is not found, there is no return value from the function.
    return -1
    #The program returns -1, indicating that `num` is not found in the sorted list of integers `arr`
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `num`. It returns the index of the first occurrence of `num` in `arr` if found; otherwise, it returns -1 if `num` is not present in the list. There are no checks for duplicate values, so if there are multiple occurrences of `num`, it always returns the index of the first one. If the list is empty, the function will return -1.

