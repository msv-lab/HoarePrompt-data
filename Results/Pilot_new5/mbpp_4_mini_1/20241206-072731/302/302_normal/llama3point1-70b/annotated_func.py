#State of the program right berfore the function call: arr is a sorted list of integers, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of integers, `num` may or may not be present in `arr`. If present, it is at index `i`, otherwise the loop has finished without finding `num`.
    return -1
    #The program returns -1, indicating that the number 'num' is not present in the sorted list of integers 'arr'.
#Overall this is what the function does:The function accepts a sorted list of integers `arr` and an integer `num`, returning the index of `num` if it exists in `arr`, or -1 if `num` is not present.

