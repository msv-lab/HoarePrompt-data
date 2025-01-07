#State of the program right berfore the function call: tup is a tuple containing strings.
def func_1(tup):
    return [s[-1] for s in tup]
    #The program returns a list of the last characters from each string in the tuple 'tup'
#Overall this is what the function does:The function accepts a tuple `tup` containing strings and returns a list of the last characters from each string in the tuple `tup`.

