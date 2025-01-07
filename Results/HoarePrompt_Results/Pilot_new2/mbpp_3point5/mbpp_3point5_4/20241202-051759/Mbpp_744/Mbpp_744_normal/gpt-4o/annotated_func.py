#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for item in tup:
        if item is None:
            return True
        
    #State of the program after the  for loop has been executed: `tup` is a tuple. The loop does not execute as it returns True as soon as it encounters an item that is None. Therefore, `item` remains the first item in the tuple, and `tup` does not change.
    return False
    #The program returns False
#Overall this is what the function does:The function func_1 accepts a parameter `tup`, which is a tuple. It iterates over the elements of the tuple and returns True if it encounters a None value. If no None value is found in the tuple, it returns False. The loop stops as soon as it finds a None value.

