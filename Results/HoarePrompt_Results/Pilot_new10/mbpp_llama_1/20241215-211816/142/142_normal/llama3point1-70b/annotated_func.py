#State of the program right berfore the function call: lst is a list and element is any type of object that can be compared with the items in lst.
def func_1(lst, element):
    return all(item == element for item in lst)
    #The program returns True if all items in lst are equal to element, False otherwise
#Overall this is what the function does:The function accepts a list `lst` and an `element`, and returns `True` if all items in `lst` are equal to `element` or if `lst` is empty, and `False` otherwise

