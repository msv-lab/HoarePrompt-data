#State of the program right berfore the function call: arr is a list of two lists, where the first list (arr[0]) contains n non-decreasing integers representing the difficulties of the initial problems (a_1, a_2, ..., a_n), and the second list (arr[1]) contains n non-decreasing integers representing the maximum expected difficulties (b_1, b_2, ..., b_n).
def func_1(arr):
    return sorted(arr, reverse=True)
    #The program returns a list of two lists, where the first list contains the difficulties (a_1, a_2, ..., a_n) in descending order, and the second list contains the maximum expected difficulties (b_1, b_2, ..., b_n) in descending order.
#Overall this is what the function does:The function `func_1` takes a list of two lists as input, where the first list contains non-decreasing integers representing the difficulties of problems, and the second list contains non-decreasing integers representing the maximum expected difficulties. After sorting both lists in descending order, it returns a new list of two lists with the difficulties and maximum expected difficulties sorted in descending order.

