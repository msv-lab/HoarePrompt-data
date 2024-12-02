#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for item in tup:
        if item is None:
            return True
        
    #State of the program after the  for loop has been executed: `tup` is a tuple. The items in the tuple are either all None or at least one item is not None. The function returns True only if all items in the tuple are None.
    return False
    #The program returns False
#Overall this is what the function does:The function func_1 accepts a tuple `tup` and returns True only if all items in the tuple are None; otherwise, it returns False. The annotations mention returning True in multiple cases, but the actual code only returns True if all items in the tuple are None.

