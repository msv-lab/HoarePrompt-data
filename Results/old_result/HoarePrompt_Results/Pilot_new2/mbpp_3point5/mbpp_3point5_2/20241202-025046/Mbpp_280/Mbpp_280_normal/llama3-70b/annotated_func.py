#State of the program right berfore the function call: arr is a list and elem is any data type.**
def func_1(arr, elem):
    for (i, x) in enumerate(arr):
        if x == elem:
            return True, i
        
    #State of the program after the  for loop has been executed: If `elem` is found in `arr`, the function returns True along with the index of the first occurrence of `elem` in the list. If `elem` is not found, the function returns False.
    return False, -1
    #The program returns False along with the index of -1 if `elem` is not found in list `arr`
#Overall this is what the function does:The function `func_1` accepts two parameters, a list `arr`, and an element `elem` of any data type. It iterates through the list to find the first occurrence of `elem`. If `elem` is found, the function returns True along with the index of that element in the list. If `elem` is not found, the function returns False along with the index of -1. The functionality does not cover the cases mentioned in the annotations where `elem` is found at specific indices (0, 1, 2) as the function only returns the first occurrence.

