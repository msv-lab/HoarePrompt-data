#State of the program right berfore the function call: array is a list of elements, and element can be of any type.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True indicating the presence of 'element' in 'array', along with the corresponding index of its first occurrence.
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: `array` is a list of elements, `element` can be of any type. If the `element` is found, the function returns `True` and the index of its first occurrence; if the `element` is not found, the function returns `False` and -1.
#Overall this is what the function does:The function `func_1` accepts a list called `array` and an element of any type. It attempts to find the index of the first occurrence of `element` in `array`. If the `element` is found, the function returns a tuple containing `True` and the index of the element. If the `element` is not found, it raises a `ValueError` and subsequently returns a tuple containing `False` and -1. The function handles missing values by returning -1 for the index when the element does not exist in the array, indicating the search was unsuccessful. Additionally, it does not account for any modifications to the array after the search or any side effects resulting from finding or not finding the element.

