#State of the program right berfore the function call: arr is a list and elem is any data type.**
def func_1(arr, elem):
    for (i, x) in enumerate(arr):
        if x == elem:
            return True, i
        
    #State of the program after the  for loop has been executed: If the loop executes, the output state will be True and the index of the first occurrence of elem in arr. If elem is not present in arr, the output state will be False. If arr is an empty list, the output state will be False.
    return False, -1
    #The program returns False and -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` and a data `elem`. It then iterates through the list to find the first occurrence of `elem`. If `elem` is found, the function returns True along with the index of `elem` in the list. If `elem` is not found, the function returns False along with -1. The functionality description provided in the annotations covers the cases where `elem` is found at different positions in the list, but it doesn't cover the case where the list `arr` is empty. In that case, the function will always return False and -1.

