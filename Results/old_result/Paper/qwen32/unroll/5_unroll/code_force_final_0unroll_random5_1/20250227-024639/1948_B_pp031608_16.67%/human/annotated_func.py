#State of the program right berfore the function call: lst is a list of integers where each integer is between 0 and 99 inclusive, and the length of lst is between 2 and 50 inclusive. This list represents the array a for a single test case. The function will be called multiple times, once for each test case, and the number of test cases t is between 1 and 1000 inclusive.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if `lst` is already sorted in non-decreasing order, otherwise it returns False.
#Overall this is what the function does:The function checks if the input list `lst` of integers is sorted in non-decreasing order and returns `True` if it is, otherwise it returns `False`.

