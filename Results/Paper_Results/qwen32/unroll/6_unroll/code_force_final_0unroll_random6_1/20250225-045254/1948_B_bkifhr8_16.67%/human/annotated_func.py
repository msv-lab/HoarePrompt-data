#State of the program right berfore the function call: lst is a list of integers where each integer a_i satisfies 0 <= a_i <= 99, and the length of lst, n, satisfies 2 <= n <= 50. This list represents the array a for a single test case in a series of t test cases, where 1 <= t <= 10^3.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if `lst` is already sorted in non-decreasing order, otherwise it returns False.
#Overall this is what the function does:The function checks if the input list `lst` of integers is sorted in non-decreasing order and returns `True` if it is, otherwise it returns `False`.

