#State of the program right berfore the function call: lst is a list of elements, and element is a value that can be of any type.
def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is a list where all elements are equal to `element`, or the function has returned False if any element was not equal to `element`.
    return True
    #The program returns True, indicating that all elements in the list 'lst' are equal to 'element'
#Overall this is what the function does:The function accepts a list `lst` and a value `element`, returning True if all elements in `lst` are equal to `element`. If any element in `lst` is not equal to `element`, it returns False. If `lst` is empty, the function will also return True, as there are no elements that contradict the condition.

