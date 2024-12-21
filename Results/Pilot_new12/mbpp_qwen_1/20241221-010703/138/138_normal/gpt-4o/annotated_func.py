#State of the program right berfore the function call: arr is a list of elements, and element is the value to search for in the list arr.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements, `element` is the value to search for in the list `arr`, `value` is the last element in the list `arr`, `index` is the index of the last element in the list (length of `arr` - 1), and the function returns `True` and `index` if the `element` is found in the list `arr`, otherwise it returns `False` and `None` if the loop completes without finding the `element`.
    return False, -1
    #The program returns False and -1
#Overall this is what the function does:The function `func_1` accepts two parameters: `arr`, which is a list of elements, and `element`, which is the value to search for in the list `arr`. The function searches for the `element` in the list `arr` using a for loop. If the `element` is found at any index in the list, the function returns `True` and the index of the `element`. If the `element` is not found in the list, the function returns `False` and `-1`.

After the function concludes, the state of the program will be as follows:
- If the `element` is found at any index in the list, the program returns `True` and the index of the `element`.
- If the `element` is not found in the list, the program returns `False` and `-1`.

Potential edge cases:
- The function correctly handles the case where the `element` is found at index 0, 1, or 2.
- The function correctly handles the case where the `element` is not found in the list, returning `False` and `-1`.

Missing functionality:
- The provided code does not handle the scenario where the `element` is found at any index other than 0, 1, or 2. While the function does return `True` and the correct index when the `element` is found, it does not specify what happens if the `element` is found at an index greater than 2. Therefore, the function always returns the index of the first occurrence of the `element` in the list, regardless of its position.

