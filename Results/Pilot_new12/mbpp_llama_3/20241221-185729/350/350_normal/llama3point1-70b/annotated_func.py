#State of the program right berfore the function call: arr is a sorted list of elements, and target is an element that may be present in arr.
def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of elements, `target` is an element that may or may not be present in `arr`, and if `target` is in `arr`, the function returns its index; otherwise, the function ends without an explicit return value.
    return -1
    #The program returns -1, indicating that the target element was not found in the sorted list arr.
#Overall this is what the function does:The function accepts a sorted list `arr` and a target element `target`, and returns the last index of the `target` element in `arr` if found. If the `target` is not found, it returns -1. The function does not modify the input list `arr` or the `target` element. The function's return value is an integer, which is either the last index of the `target` element in `arr` or -1 to indicate that the `target` was not found. The function handles edge cases where the `target` element is not present in `arr`, and it also correctly handles cases where `arr` is empty or contains only one element. The return postconditions in the annotations, specifically Case_2 and Case_3, do not accurately reflect the code's behavior, as the code only returns the last index of the `target` element or -1.

