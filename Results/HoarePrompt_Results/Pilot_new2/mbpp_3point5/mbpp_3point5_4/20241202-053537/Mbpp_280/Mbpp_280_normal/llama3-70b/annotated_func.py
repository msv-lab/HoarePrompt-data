#State of the program right berfore the function call: arr is a list of elements and elem is the element to be searched in arr.**
def func_1(arr, elem):
    for (i, x) in enumerate(arr):
        if x == elem:
            return True, i
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, if the element `elem` is found in the list `arr`, the program will return True and the index `i` where the element `elem` is found. If `elem` is not found in `arr`, the program will not return anything.
    return False, -1
    #The program returns False, -1 as the default values when the element 'elem' is not found in the list 'arr'
#Overall this is what the function does:The function `func_1` takes in a list `arr` of elements and an element `elem` to be searched in the list. It then iterates through the list using a for loop and returns True along with the index `i` of the element `elem` if it is found in the list. If the element is not found, the function returns False along with -1 as default values. The function correctly handles the cases where the element is found at the beginning or somewhere in the middle of the list.

