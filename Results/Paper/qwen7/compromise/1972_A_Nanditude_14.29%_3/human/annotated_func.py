#State of the program right berfore the function call: arr is a list of two lists, where the first list contains n non-decreasing integers representing the difficulties of the initial problems (a_1, a_2, ..., a_n), and the second list contains n non-decreasing integers representing the expected maximum difficulties (b_1, b_2, ..., b_n), with 1 ≤ n ≤ 100 and 1 ≤ a_i, b_i ≤ 10^9.
def func_1(arr):
    return sorted(arr, reverse=True)
    #The program returns a list of two lists, where the first list contains the difficulties of the initial problems in non-increasing order, and the second list contains the expected maximum difficulties in non-increasing order.
#Overall this is what the function does:The function accepts a list of two lists, where the first list contains non-decreasing integers representing the difficulties of the initial problems, and the second list contains non-decreasing integers representing the expected maximum difficulties. After sorting both lists in non-increasing order, it returns a new list of two lists with the same structure.

