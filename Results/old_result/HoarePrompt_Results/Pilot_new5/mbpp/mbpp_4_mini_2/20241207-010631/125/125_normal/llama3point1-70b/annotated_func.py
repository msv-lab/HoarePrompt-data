#State of the program right berfore the function call: lst is a list of elements, and n is a positive integer greater than 0.
def func_1(lst, n):
    return [lst[i::n] for i in range(n)]
    #The program returns a list of sublists, where each sublist contains elements from 'lst' taken every 'n' elements starting from index 'i', for each 'i' in the range of 'n'
#Overall this is what the function does:The function accepts a list `lst` and a positive integer `n`, and returns a list of sublists, where each sublist contains elements from `lst` taken every `n` elements starting from each index `i` in the range of `n`. If `n` is greater than the length of `lst`, the resulting sublists may contain fewer elements, but the function will still operate as intended without errors.

