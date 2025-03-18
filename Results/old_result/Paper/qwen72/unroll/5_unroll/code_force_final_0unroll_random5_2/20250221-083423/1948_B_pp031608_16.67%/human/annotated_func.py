#State of the program right berfore the function call: lst is a list of integers where each integer is between 0 and 99 inclusive, and the length of lst is between 2 and 50 inclusive.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns False if `lst` is not already sorted in ascending order, and True if `lst` is already sorted in ascending order.
#Overall this is what the function does:The function `func_1` accepts a list `lst` of integers (each between 0 and 99, and the list length between 2 and 50) and returns `True` if the list is already sorted in ascending order. If the list is not sorted in ascending order, it returns `False`. The function does not modify the input list `lst`.

