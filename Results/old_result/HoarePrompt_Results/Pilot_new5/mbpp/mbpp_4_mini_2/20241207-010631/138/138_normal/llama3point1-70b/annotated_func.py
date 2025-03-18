#State of the program right berfore the function call: array is a list of elements and element is a value that may be present in the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True indicating that the 'element' is present in the 'array', along with its index in the 'array'
    except (ValueError):
        return False, -1
        #The program returns a tuple containing False and -1
    #State of the program after the try-except block has been executed: `array` is a list of elements, and `element` is a value that may or may not be present in the `array`. If the element is found, the function returns a tuple containing `True` and the index of the element; if not found, it returns a tuple containing `False` and -1.
#Overall this is what the function does:The function accepts a list `array` and a value `element`. It attempts to find the index of `element` in `array`. If `element` is found, it returns a tuple containing `True` and the index of the element. If `element` is not found, it catches the `ValueError` and returns a tuple containing `False` and -1. The function correctly handles the case where the element is not present in the list by returning a specific tuple indicating the absence.

