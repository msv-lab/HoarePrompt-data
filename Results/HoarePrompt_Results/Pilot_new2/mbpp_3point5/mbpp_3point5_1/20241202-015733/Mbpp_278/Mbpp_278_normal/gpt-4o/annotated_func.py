#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        
        count += 1
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, `count` is the number of elements in `tup` before the first occurrence of a tuple. If a tuple is encountered, the loop breaks.
    return count
    #The program returns the number of elements in `tup` before the first occurrence of a tuple. If a tuple is encountered, the loop breaks.
#Overall this is what the function does:The function `func_1` accepts a parameter `tup`, which is a tuple. It iterates through the elements of the tuple `tup` and returns the number of elements in `tup` before the first occurrence of a tuple. If a tuple is encountered during the iteration, the loop breaks. Therefore, the functionality of the function is to return the count of elements before the first tuple in the tuple `tup`.

