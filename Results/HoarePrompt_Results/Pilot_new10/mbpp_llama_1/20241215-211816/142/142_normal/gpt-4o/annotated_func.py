#State of the program right berfore the function call: lst is a list and element is any type of object that can be compared to the elements in the list.
def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is a list where either all items are equal to `element`, or the function has returned `False` due to an item not equal to `element`; if `lst` is empty, the function does not execute and implicitly moves on or returns an implicit value like `None`.
    return True
    #The program returns True, indicating that all items in the list `lst` are equal to `element`, since the function has not returned False due to an item not equal to `element`.
#Overall this is what the function does:The function accepts a list `lst` and an `element`, returns `True` if all items in `lst` are equal to `element` or if `lst` is empty, and returns `False` otherwise.

