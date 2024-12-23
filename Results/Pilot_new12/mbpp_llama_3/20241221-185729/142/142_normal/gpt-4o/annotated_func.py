#State of the program right berfore the function call: lst is a list and element can be of any type that can be compared for equality with the elements in lst.
def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is a list, and if `lst` is not empty, either all elements in `lst` are equal to `element` (in which case the loop completes without returning False), or the loop returns False as soon as it encounters an element not equal to `element`. If `lst` is empty, the loop does not execute.
    return True
    #The program returns True, indicating that the list `lst` is either empty or all elements in `lst` are equal to `element`.
#Overall this is what the function does:The function accepts a list `lst` and an `element`, and returns `True` if `lst` is empty or all elements in `lst` are equal to `element`, otherwise returns `False`. This includes edge cases such as an empty list, a list with a single element, a list with multiple elements, and elements of any type that can be compared for equality. The function does not modify the input list or element, and its return value indicates whether the list contains only the specified element or is empty.

