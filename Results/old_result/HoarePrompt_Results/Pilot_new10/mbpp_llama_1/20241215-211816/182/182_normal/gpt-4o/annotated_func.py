#State of the program right berfore the function call: tup is a tuple containing strings.
def func_1(tup):
    return [s[-1] for s in tup]
    #The program returns a list containing the last characters of all the strings in the tuple `tup`.
#Overall this is what the function does:The function accepts a tuple of strings, returns a list of the last characters of each non-empty string in the tuple, and raises an IndexError if any string in the tuple is empty. If the tuple is empty, it returns an empty list.

