#State of the program right berfore the function call: lst is a list of lists, where each sublist contains n integers (2 ≤ n ≤ 50) and each integer a_i satisfies 0 ≤ a_i ≤ 99. The outer list lst contains t sublists (1 ≤ t ≤ 10^3), where each sublist represents the array a for a separate test case.
def func_1(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
    #The program returns True if lst is already sorted in lexicographical order, otherwise it returns False.
#Overall this is what the function does:The function accepts a parameter `lst`, which is a list of lists. Each sublist contains integers between 0 and 99. The function returns `True` if all the sublists in `lst` are sorted in lexicographical order; otherwise, it returns `False`.

