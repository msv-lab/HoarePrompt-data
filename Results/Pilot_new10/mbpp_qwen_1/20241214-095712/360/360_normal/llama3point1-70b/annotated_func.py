#State of the program right berfore the function call: lists is a list of lists of integers.
def func_1(lists):
    return max(lists, key=sum)
    #The program returns a list from `lists` which has the maximum sum when the elements of each sublist are added together
#Overall this is what the function does:The function accepts a list of lists of integers and returns the sublist with the highest sum of its elements. If multiple sublists have the same highest sum, it returns one of them.

