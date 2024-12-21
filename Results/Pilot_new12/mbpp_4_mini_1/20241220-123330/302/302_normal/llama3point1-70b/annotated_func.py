#State of the program right berfore the function call: arr is a sorted list of integers, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of integers, `num` is an integer, if `num` is present in `arr`, the function returns the index of `num` in `arr`; if `num` is not present, the function has no return value, and `i` is equal to the length of `arr` with `x` being the value at that index, or there are no integers in `arr` if the loop does not execute, making `i` undefined.
    return -1
    #The program returns -1, indicating that 'num' is not present in the sorted list 'arr' of integers.
#Overall this is what the function does:The function `func_1` takes a sorted list of integers `arr` and an integer `num` as parameters. It searches for the first occurrence of `num` in `arr` and returns its index. If `num` is found, the function returns the index of its first occurrence. If `num` is not present in `arr`, the function returns -1. Edge cases include the scenario where `arr` is empty, in which case the function will also return -1, since there will be no elements to match against `num`. The function does not handle any potential exceptions that may arise from invalid input types for `arr` and `num` but operates under the assumption that `arr` is a list of integers and `num` is an integer.

