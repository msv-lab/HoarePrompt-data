#State of the program right berfore the function call: lst is a list of elements, and element can be of any type.
def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is a list of elements that may contain any type, `item` is equal to `element` for all elements in `lst`, and the loop has finished executing without returning False. If `lst` is empty, the loop does not execute, and no element comparisons occur.
    return True
    #The program returns True, indicating that the loop has finished executing without returning False for all elements in the list `lst`, which may contain any type.
#Overall this is what the function does:The function accepts a list `lst` and an `element`. It returns `True` if all elements in `lst` are equal to `element` or if `lst` is empty. It returns `False` if any element in `lst` is not equal to `element`.

