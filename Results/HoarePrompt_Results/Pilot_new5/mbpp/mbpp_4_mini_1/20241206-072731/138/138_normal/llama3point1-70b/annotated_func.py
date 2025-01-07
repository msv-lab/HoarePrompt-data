#State of the program right berfore the function call: array is a list of elements, and element can be of any type.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and the index of 'element' in 'array'
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: `array` is a list of elements, and `element` can be of any type. If the `element` is found in the `array`, the function returns `True` and the index of the `element`; otherwise, it returns `False` and -1.
#Overall this is what the function does:The function accepts a list `array` and an arbitrary `element`. It returns `True` and the index of `element` if it is found in `array`. If `element` is not found, it returns `False` and -1. The function handles the case where the element is not present by catching a `ValueError` exception.

