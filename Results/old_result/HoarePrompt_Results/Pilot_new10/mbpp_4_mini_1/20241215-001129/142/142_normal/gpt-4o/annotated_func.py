#State of the program right berfore the function call: lst is a list of items and element is a value that may be of any type.
def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is a list where all items are equal to `element`, `item` is the last item in `lst`, `lst` has at least one item.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a list `lst` and a value `element`. It checks if all items in the list are equal to `element`. If all items match, it returns True; otherwise, it returns False. If the list is empty, the function will return True, as there are no items to contradict the condition.

