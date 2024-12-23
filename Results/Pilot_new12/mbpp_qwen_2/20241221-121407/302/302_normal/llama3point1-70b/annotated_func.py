#State of the program right berfore the function call: arr is a list of integers that is sorted in non-decreasing order, and num is an integer.
def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
        
    #State of the program after the  for loop has been executed: `arr` is a non-empty list of integers sorted in non-decreasing order, `i` is the index of the last iteration, `x` is the last element of `arr` checked, and if `num` is found in `arr`, the function returns the index where `num` is found. If `num` is not found in `arr`, the function returns `None`.
    return -1
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers sorted in non-decreasing order and an integer `num`. It searches for `num` within `arr` and returns the index of `num` if found, otherwise it returns `None`. Specifically:
- The function iterates through the list `arr` using a for loop.
- For each element `x` in `arr`, it checks if `x` equals `num`.
- If a match is found, the function immediately returns the index `i` where the match occurred.
- If no match is found after checking all elements in `arr`, the function returns `None`.

Potential edge cases and missing functionality:
- If `arr` is empty, the function will return `None` without entering the loop, which is correctly covered by the provided annotations.
- The function correctly handles the case where `num` is not found in `arr` by returning `None`.
- The function does not handle the specific return values 0, 1, or 2 mentioned in the return postconditions; these values are not reflected in the actual code logic. Therefore, the function can only return `None` when `num` is not found, or the index of `num` when it is found.

