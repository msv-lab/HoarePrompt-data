#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        
        count += 1
        
    #State of the program after the  for loop has been executed: `tup` has at least 5 elements, `count` is the total number of elements in `tup`, `elem` is the fifth element in `tup`. If `elem` is a tuple, we break out of the most internal loop or if statement. Otherwise, no changes occur.
    return count
    #The program returns the total number of elements in `tup`
#Overall this is what the function does:The function func_1 accepts a tuple `tup` as a parameter and returns the total number of elements in the tuple. It iterates over the elements of the tuple until it encounters a tuple element, at which point it stops counting and returns the total count of elements encountered so far. However, there is a missing condition where the function should handle cases where there are no tuple elements in the tuple `tup` as it currently does not account for this scenario.

