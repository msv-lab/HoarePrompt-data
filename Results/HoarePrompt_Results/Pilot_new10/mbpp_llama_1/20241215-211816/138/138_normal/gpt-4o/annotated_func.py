#State of the program right berfore the function call: arr is a list and element is any type of object that can be compared for equality.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list, `element` is any type of object, if `arr` contains `element`, the function returns `True` and the index of the first occurrence of `element`; otherwise, it implicitly returns `None`, with `index` and `value` reflecting the last element of `arr` if `arr` is not empty, or their original state if `arr` is empty.
    return False, -1
    #The program returns False and -1
#Overall this is what the function does:The function accepts a list and an element, returning a tuple containing True and the index of the element if it exists in the list, or False and -1 if it does not, covering cases for empty lists and lists with duplicate elements.

