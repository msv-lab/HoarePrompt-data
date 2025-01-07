#State of the program right berfore the function call: arr is a list of integers or other hashable elements, and element is a single integer or hashable element.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a non-empty list of integers or other hashable elements, `element` is the searched element, `index` is the index of the first occurrence of `element` in `arr` if `element` is found, otherwise `index` is `None`.
    return False, -1
    #The program returns False and -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` and a single element `element`. It searches for the first occurrence of `element` in `arr` and returns `True` along with the index of `element` if found. If `element` is found at positions 0, 1, or 2, it returns `True` and the corresponding index. If `element` is not found in `arr`, it returns `False` and `-1`.

