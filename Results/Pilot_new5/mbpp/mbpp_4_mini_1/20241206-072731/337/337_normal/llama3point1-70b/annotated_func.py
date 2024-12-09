#State of the program right berfore the function call: lst is a list of integers.
def func_1(lst):
    return sum(i for i in lst if lst.count(i) == 1)
    #The program returns the sum of integers in the list 'lst' that appear exactly once.
#Overall this is what the function does:The function accepts a list of integers `lst` and returns the sum of integers that appear exactly once in the list. If all integers appear more than once, it will return 0 as the sum of an empty list is 0. Note that the function does not account for the case where `lst` is empty, but it will return 0 in that case as well.

