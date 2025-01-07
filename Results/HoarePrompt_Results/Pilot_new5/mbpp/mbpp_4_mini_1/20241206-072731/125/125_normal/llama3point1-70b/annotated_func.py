#State of the program right berfore the function call: lst is a list of elements, and n is a positive integer greater than 0.
def func_1(lst, n):
    return [lst[i::n] for i in range(n)]
    #The program returns a list containing sublists of 'lst', where each sublist consists of elements taken from 'lst' starting at index 'i' and continuing in steps of 'n', for each 'i' in the range from 0 to n-1.
#Overall this is what the function does:The function accepts a list `lst` and a positive integer `n`, and returns a list of sublists, where each sublist consists of elements taken from `lst` starting at each index from 0 to n-1 and continuing in steps of `n`. It assumes that `n` is greater than 0 and does not handle cases where `lst` is empty, which would result in a list of empty sublists.

