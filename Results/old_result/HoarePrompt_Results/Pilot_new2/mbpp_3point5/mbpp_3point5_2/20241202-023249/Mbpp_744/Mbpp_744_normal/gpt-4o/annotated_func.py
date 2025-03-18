#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for item in tup:
        if item is None:
            return True
        
    #State of the program after the  for loop has been executed: `tup` is a tuple with all non-None items. If any item in `tup` is None, the function returns True. Otherwise, the function returns None.
    return False
    #The program returns False
#Overall this is what the function does:Functionality: The function `func_1` accepts a parameter `tup`, which is a tuple. It iterates through the tuple and if it encounters a `None` value, it returns True. Otherwise, it returns False. The function will always return False if there are no `None` values in the tuple.

