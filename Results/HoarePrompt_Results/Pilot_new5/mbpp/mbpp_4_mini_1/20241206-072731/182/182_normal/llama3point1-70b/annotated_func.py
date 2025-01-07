#State of the program right berfore the function call: strings is a tuple of strings.
def func_1(strings):
    return [s[-1] for s in strings]
    #The program returns a list containing the last character of each string in the tuple 'strings'
#Overall this is what the function does:The function accepts a tuple of strings and returns a list containing the last character of each string. If any string in the tuple is empty, it will raise an IndexError since it attempts to access the last character of that string.

