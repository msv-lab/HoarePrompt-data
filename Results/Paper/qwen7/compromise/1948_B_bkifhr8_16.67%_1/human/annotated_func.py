#State of the program right berfore the function call: lst is a list of integers, where each integer is between 0 and 99 inclusive, and the length of the list is between 2 and 50.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if the list 'lst' is already sorted in ascending order, otherwise it returns False.
#Overall this is what the function does:The function accepts a list of integers (where each integer is between 0 and 99 inclusive, and the length of the list is between 2 and 50) and returns True if the list is already sorted in ascending order, otherwise it returns False.

