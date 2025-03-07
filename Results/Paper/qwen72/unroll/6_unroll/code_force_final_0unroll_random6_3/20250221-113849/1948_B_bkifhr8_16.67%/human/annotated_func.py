#State of the program right berfore the function call: lst is a list of integers where each integer is between 0 and 99 inclusive, and the length of lst is between 2 and 50 inclusive.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns False if the original list `lst` was not already sorted in ascending order, and returns True if `lst` was already sorted in ascending order.
#Overall this is what the function does:The function `func_1` accepts a list `lst` of integers (each between 0 and 99, and the list length between 2 and 50). It returns `True` if the original list `lst` is sorted in ascending order, and `False` otherwise. The function does not modify the original list `lst`.

