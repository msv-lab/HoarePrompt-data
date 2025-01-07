#State of the program right berfore the function call: list1 and list2 are lists.**
def func_1(list1, list2):
    return sorted(list(set(list1) ^ set(list2)))
    #The program returns a sorted list of unique elements that are present in either list1 or list2, but not in both
#Overall this is what the function does:The function accepts two lists, list1 and list2, and returns a sorted list of unique elements that are present in either list1 or list2, but not in both. The function first combines the elements of list1 and list2, removes duplicates, and then sorts the resulting list before returning it.

