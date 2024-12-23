#State of the program right berfore the function call: arr is a list, and element can be of any data type.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list, if `element` is in `arr`, the output will be True and the index of the first occurrence of the `element`, otherwise the function does not return a value. `index` is the last index checked, and `value` is the last element checked in `arr`.
    return False, -1
    #The program returns False and -1, indicating that the element is not in the list 'arr' and there is no valid index for the element.
#Overall this is what the function does:The function `func_1` accepts a list `arr` and an `element`. It searches for the first occurrence of `element` in `arr`. If found, it returns `True` along with the index of the first occurrence. If not found, it returns `False` and `-1`. The function properly handles cases where `arr` is empty or where `element` is not present. The annotations regarding the return values for different cases are mostly accurate but suggest a limitation based on the number of elements checked, which is not the actual behavior of the function. The function will search all elements in `arr`, not just the first three, and will return appropriate values based on the presence or absence of `element`.

