#State of the program right berfore the function call: lst is a list of integers where each integer a_i satisfies 0 <= a_i <= 99, and the length of lst is an integer n such that 2 <= n <= 50. This list represents the array a for a single test case. The function will be called multiple times, once for each test case, with different lists. The number of test cases, t, satisfies 1 <= t <= 10^3.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if lst is already sorted in non-decreasing order, otherwise it returns False.
#Overall this is what the function does:The function accepts a list of integers, `lst`, where each integer is between 0 and 99, and the length of the list is between 2 and 50. It returns `True` if the list is sorted in non-decreasing order; otherwise, it returns `False`.

