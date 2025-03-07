#State of the program right berfore the function call: lst is a list of integers where each integer a_i satisfies 0 <= a_i <= 99, and the length of lst, n, satisfies 2 <= n <= 50. Additionally, the function will be called multiple times (t times) with each call receiving a separate list lst as described, where 1 <= t <= 10^3.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if the list `lst` is already sorted in non-decreasing order, otherwise it returns False.
#Overall this is what the function does:The function checks if a given list of integers, where each integer is between 0 and 99 and the list length is between 2 and 50, is sorted in non-decreasing order. It returns `True` if the list is sorted, otherwise it returns `False`.

