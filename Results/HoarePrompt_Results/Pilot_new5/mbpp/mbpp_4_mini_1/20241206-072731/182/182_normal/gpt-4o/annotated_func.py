#State of the program right berfore the function call: tup is a tuple of strings.
def func_1(tup):
    return [s[-1] for s in tup]
    #The program returns a list containing the last character of each string in the tuple 'tup'
#Overall this is what the function does:The function accepts a tuple of strings and returns a list containing the last character of each string in the tuple. If any string in the tuple is empty, the function will raise an IndexError because it attempts to access the last character of that string.

