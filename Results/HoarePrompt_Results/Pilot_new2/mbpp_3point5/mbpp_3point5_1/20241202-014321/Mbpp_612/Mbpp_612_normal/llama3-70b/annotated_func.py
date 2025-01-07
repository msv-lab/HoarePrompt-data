#State of the program right berfore the function call: list_of_lists is a list of lists where each sublist has exactly two elements.**
def func_1(list_of_lists):
    return [list(element[0] for element in list_of_lists), list(element[1] for
    element in list_of_lists)]
    #The program returns two lists: one containing the first elements of each sublist in list_of_lists and the other containing the second elements of each sublist in list_of_lists
#Overall this is what the function does:The function accepts a parameter list_of_lists, and it returns two lists—one containing the first elements and the other containing the second elements of each sublist in list_of_lists. The function correctly extracts the first and second elements of each sublist in the input list_of_lists.

