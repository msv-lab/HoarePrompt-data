#State of the program right berfore the function call: sublists is a list of lists.
def func_1(sublists):
    return [sublist[0] for sublist in sublists]
    #The program returns a list containing the first element of each sublist in the list 'sublists'
#Overall this is what the function does:The function accepts a list of lists called `sublists` and returns a new list containing the first element of each sublist. If any sublist is empty, it will raise an `IndexError` because it attempts to access the first element of an empty list.

