#State of the program right berfore the function call: lst is a list of integers where each integer is between 0 and 99 inclusive, and the length of lst is between 2 and 50 inclusive. This list represents the array a for a single test case. The function will be called multiple times, each time with a different list representing a different test case, and the number of such test cases is between 1 and 1000 inclusive.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if the original list `lst` is already sorted in non-decreasing order, otherwise it returns False.
#Overall this is what the function does:The function takes a list of integers, where each integer is between 0 and 99 inclusive and the list length is between 2 and 50 inclusive, and returns `True` if the list is already sorted in non-decreasing order; otherwise, it returns `False`.

