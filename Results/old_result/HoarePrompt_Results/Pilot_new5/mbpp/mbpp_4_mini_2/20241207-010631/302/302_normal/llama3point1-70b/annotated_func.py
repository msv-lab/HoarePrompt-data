#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `i` is the length of `arr`, `x` is the value of the last integer in `arr`, and `num` is not present in `arr`.
    return -1
    #The program returns -1, indicating that 'num' is not present in the sorted list 'arr' of integers.
#Overall this is what the function does:The function accepts a list of integers `arr` sorted in non-decreasing order and an integer `num`. It returns the index of the first occurrence of `num` in `arr` if found. If `num` is not present in `arr`, it returns -1. The function does not handle cases where `arr` is empty, but it will correctly return -1 in such instances, indicating that `num` is not found.

