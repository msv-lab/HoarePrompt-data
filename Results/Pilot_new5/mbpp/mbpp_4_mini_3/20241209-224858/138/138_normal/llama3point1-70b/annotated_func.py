#State of the program right berfore the function call: array is a list of elements, and element can be of any type that is comparable to the elements in the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and the index of 'element' in 'array', indicating that 'element' is present in 'array'
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: `array` is a list of elements, and `element` can be of any type that is comparable to the elements in the `array`. If the `element` is present in the `array`, the function returns `True` and its index; otherwise, it returns `False` and `-1.`
#Overall this is what the function does:The function accepts a list `array` and an `element` of any type that is comparable to the elements in the list. It returns `True` and the index of `element` if it is found in `array`; otherwise, it returns `False` and `-1`. The function handles cases where the `element` is not present by using exception handling for `ValueError`.

