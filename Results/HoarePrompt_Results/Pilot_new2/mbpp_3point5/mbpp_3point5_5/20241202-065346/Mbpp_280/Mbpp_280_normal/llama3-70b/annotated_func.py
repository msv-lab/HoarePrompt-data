#State of the program right berfore the function call: arr is a list and elem is any valid python data type.**
def func_1(arr, elem):
    for (i, x) in enumerate(arr):
        if x == elem:
            return True, i
        
    #State of the program after the  for loop has been executed: If the loop executes, arr is a list with at least one element, elem is any valid python data type, and the function returns True and the index of the first occurrence of elem in arr. If elem is not found in arr, the function returns False. If the loop does not execute, arr can be an empty list and the function will return False since elem is not found.
    return False, -1
    #The program returns False and -1, as the loop does not execute and elem is not found in the list arr
#Overall this is what the function does:The function `func_1` accepts a list `arr` and an element `elem`. It then iterates through the list to find the first occurrence of `elem`. If `elem` is found, it returns True along with the index of the element in the list. If `elem` is not found, it returns False and -1. The function covers cases where `elem` is found at different indices in the list.

