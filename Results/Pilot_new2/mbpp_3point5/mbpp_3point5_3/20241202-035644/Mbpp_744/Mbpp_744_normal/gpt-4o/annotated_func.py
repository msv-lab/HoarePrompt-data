#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for item in tup:
        if item is None:
            return True
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple. The loop will only execute once at most, and `item` will be the first non-None element in `tup`. If the first element in `tup` is None, the function will return True.
    return False
    #The program returns False
#Overall this is what the function does:The function func_1 accepts a tuple `tup` and iterates through its elements. If the first non-None element in `tup` is encountered, the function returns True. If there are no non-None elements in `tup`, the function returns False.

