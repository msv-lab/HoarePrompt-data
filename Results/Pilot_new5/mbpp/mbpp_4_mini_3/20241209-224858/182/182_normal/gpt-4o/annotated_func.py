#State of the program right berfore the function call: tup is a tuple of strings.
def func_1(tup):
    return [s[-1] for s in tup]
    #The program returns a list of the last character from each string in the tuple 'tup'
#Overall this is what the function does:The function accepts a tuple of strings and returns a list of the last character from each string in the tuple. If any string in the tuple is empty, it will result in an IndexError since there is no last character to retrieve.

