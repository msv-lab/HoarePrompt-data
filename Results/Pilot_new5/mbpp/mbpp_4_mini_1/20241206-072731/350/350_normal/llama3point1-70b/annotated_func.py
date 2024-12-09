#State of the program right berfore the function call: arr is a sorted list of elements, and target is the element whose last position needs to be found in arr.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: arr is a sorted list of elements, `i` is -1, and if `target` is not found in `arr`, the function does not return any value. If `target` is present, `i` would have been the index of the last occurrence of `target` in `arr`.
    return -1
    #The program returns -1, indicating that the target is not found in the sorted list `arr`, and `i` remains -1.
#Overall this is what the function does:The function accepts a sorted list `arr` and an element `target`, returning the index of the last occurrence of `target` in `arr`. If `target` is not found, it returns -1. The function does not handle cases where `arr` is empty, but it will correctly return -1 for such scenarios as well. Additionally, it assumes that `arr` contains comparable elements and does not handle any exceptions that might arise from invalid comparisons.

