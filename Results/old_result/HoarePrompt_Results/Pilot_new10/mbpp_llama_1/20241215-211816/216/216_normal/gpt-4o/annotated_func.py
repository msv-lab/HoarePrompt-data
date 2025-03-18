#State of the program right berfore the function call: lst is a list of integers.
def func_1(lst):
    if (not lst) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: lst is a list of integers, and the list is not empty
    lst_sorted = sorted(lst)
    for i in range(len(lst_sorted) - 1):
        if lst_sorted[i + 1] - lst_sorted[i] != 1:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is the original list of integers, `lst_sorted` is a sorted list of consecutive integers equal to `lst`, and if `lst` has at least 2 elements, the loop completes with `i` being the last index checked, indicating all elements in `lst_sorted` are consecutive; if `lst` has less than 2 elements, the loop does not execute, and `lst` and `lst_sorted` remain unchanged.
    return True
    #The program returns True, indicating that the list `lst_sorted` contains consecutive integers and is equal to the original list `lst`.
#Overall this is what the function does:The function accepts a list of integers and returns True if the list is non-empty and contains consecutive integers in any order, or if the list contains a single element; it returns False for an empty list or a list where any two adjacent elements in sorted order are not consecutive

