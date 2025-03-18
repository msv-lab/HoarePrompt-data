#State of the program right berfore the function call: a and b are lists of integers of the same length n, where 1 ≤ n ≤ 100, and both a and b are sorted in non-decreasing order. Each element in a and b satisfies 1 ≤ a_i, b_i ≤ 10^9.
def func_1(arr):
    return sorted(arr, reverse=True)
    #The program returns the list `arr` sorted in non-increasing order.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and returns the same list sorted in non-increasing order. The input list `arr` is not modified, and the function does not have any side effects on other variables or the program state.

