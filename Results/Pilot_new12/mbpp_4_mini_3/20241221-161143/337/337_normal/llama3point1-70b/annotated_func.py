#State of the program right berfore the function call: lst is a list of integers.
def func_1(lst):
    return sum(i for i in lst if lst.count(i) == 1)
    #The program returns the sum of all integers in the list 'lst' that appear exactly once.
#Overall this is what the function does:The function accepts a single parameter `lst`, which is a list of integers. It computes and returns the sum of all integers in `lst` that appear exactly once. If there are no integers that meet this criterion, the function will return `0`. The function does not modify the input list `lst`. Edge cases such as an empty list will also result in a return value of `0`, since there are no integers to sum. Additionally, any input list containing only duplicated integers will also return `0`.

