#State of the program right berfore the function call: arr is a list of sorted integers and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of sorted integers, `num` is an integer, if `num` is found in `arr`, the output is the index of `num` in `arr`; otherwise, the loop completes without finding `num`, and there is no return value from the function.
    return -1
    #The program returns -1 indicating that the integer 'num' was not found in the sorted list 'arr'.
#Overall this is what the function does:The function accepts a list of sorted integers `arr` and an integer `num`. It returns the index of `num` in `arr` if found; otherwise, it returns -1. The function performs a linear search, which does not take advantage of the sorted property of `arr`, meaning it may not be efficient for large lists.

