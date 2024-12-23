#State of the program right berfore the function call: array is a list of integers or other hashable types, and element is an integer or other hashable type.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns `True` and `index` which is the index of `element` in `array`
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: The program could raise a `ValueError` if the `element` is not found in the `array`. If the `element` is found in the `array`, the function returns `True` along with the index of the `element`. 
    #
    #Summarizing the steps and the output state:
    #
    #- The `try` block attempts to find the index of `element` in `array` using `array.index(element)`.
    #- If the `element` is found, the function returns `True` and the index of the `element`.
    #- If the `element` is not found (raises a `ValueError`), the function returns `False` and `-1`.
    #
    #Therefore, the output state is:
    #**The program returns `True` and `index` which is the index of `element` in `array`. If the `element` is not found, the function returns `False` and `-1`.**
#Overall this is what the function does:The function `func_1` accepts a list `array` and an element `element`. It attempts to find the index of `element` within `array`. If the `element` is found, the function returns `True` along with the index of the `element`. If the `element` is not found, the function returns `False` and `-1`. This covers all potential outcomes of searching for an element in the list, including the case where the element is not present.

