#State of the program right berfore the function call: array is a list of elements, and element can be any type that may or may not be present in the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and the index of 'element' in 'array' if 'element' is present; otherwise, a ValueError occurs.
    except (ValueError):
        return False, -1
        #The program returns a tuple containing False and -1
    #State of the program after the try-except block has been executed: `array` is a list of elements, and `element` can be any type. If the element is found, the function returns True and its index; if it is not found, the function returns False and -1.
#Overall this is what the function does:The function `func_1` accepts a list called `array` and an `element` of any type. It searches for the `element` in the `array`. If the `element` is found, the function returns a tuple containing `True` and the zero-based index of the `element` in the `array`. If the `element` is not found, a `ValueError` is triggered, and the function handles it by returning a tuple containing `False` and -1. The function does not modify the input `array`, and it effectively handles the case where the `element` might not be present in the list.

