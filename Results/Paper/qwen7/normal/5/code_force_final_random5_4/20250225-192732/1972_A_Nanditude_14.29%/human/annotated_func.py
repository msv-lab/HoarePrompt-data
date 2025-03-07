#State of the program right berfore the function call: arr is a list of two lists, where the first list contains n non-decreasing integers representing the difficulties of the existing problems (a_1, a_2, ..., a_n), and the second list contains n non-decreasing integers representing the expected difficulties (b_1, b_2, ..., b_n), with 1 <= n <= 100 and 1 <= a_i, b_i <= 10^9.
def func_1(arr):
    return sorted(arr, reverse=True)
    #The program returns a list of two lists, where the first list contains n non-decreasing integers and the second list contains n non-decreasing integers, but both lists are sorted in descending order.
#Overall this is what the function does:The function accepts a list of two lists, where the first list contains n non-decreasing integers representing the difficulties of existing problems and the second list contains n non-decreasing integers representing the expected difficulties. After sorting both lists in descending order, it returns a new list of two lists with the same structure but with elements sorted in descending order.

