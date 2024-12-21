#State of the program right berfore the function call: arr is a sorted list of numbers, and num is a number.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: 
    return -1
    #The program returns -1
#Overall this is what the function does:The function searches for a specific number `num` within a sorted list of numbers `arr` and returns the index of `num` if found. If `num` is not found in `arr`, the function returns -1. The function operates on the assumption that the input list `arr` is sorted, and it does not modify the original list. It handles edge cases where `num` is at any position in `arr`, including the first and last positions, as well as cases where `num` is not present in `arr`, in which case it returns -1. The function effectively performs a linear search operation on the sorted list, providing a simple and straightforward way to locate a specific number within a sorted sequence.

