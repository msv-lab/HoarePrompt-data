#State of the program right berfore the function call: arr is a list and elem is any data type.**
def func_1(arr, elem):
    for (i, x) in enumerate(arr):
        if x == elem:
            return True, i
        
    #State of the program after the  for loop has been executed: If the loop executes, `arr` is a list with at least one element equal to `elem`, and `i` is the index of the first occurrence of `elem`. If the loop does not execute, `arr` is an empty list, and `i` is None.
    return False, -1
    #The program returns False and -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` and an element `elem`, then it iterates over the list to find if any element matches `elem`. If a match is found, it returns True along with the index `i` of the first occurrence of `elem`. If no match is found, it returns False and -1. The function covers the cases where `elem` is found at different indexes in the list.

