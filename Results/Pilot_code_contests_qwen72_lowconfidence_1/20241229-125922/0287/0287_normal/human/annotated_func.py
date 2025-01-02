#State of the program right berfore the function call: lst1 and lst2 are lists of distinct integers where each integer is between 1 and 9 (inclusive), and both lists have lengths between 1 and 9 (inclusive).
def func_1(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
    #The program returns `lst3`, which is a list containing the common elements of `lst1` and `lst2`. Each element in `lst3` is an integer between 1 and 9 (inclusive), and `lst3` may contain zero or more elements depending on the overlap between `lst1` and `lst2`.
#Overall this is what the function does:The function `func_1` accepts two lists, `lst1` and `lst2`, where each list contains distinct integers between 1 and 9 (inclusive). It returns a new list, `lst3`, which contains the common elements found in both `lst1` and `lst2`. The elements in `lst3` are also integers between 1 and 9 (inclusive). If there are no common elements between `lst1` and `lst2`, `lst3` will be an empty list. The order of elements in `lst3` is the same as their order in `lst1`. The original lists `lst1` and `lst2` remain unchanged.

