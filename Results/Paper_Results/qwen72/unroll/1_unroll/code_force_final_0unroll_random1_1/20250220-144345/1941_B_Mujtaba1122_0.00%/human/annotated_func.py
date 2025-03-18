#State of the program right berfore the function call: list is a list of integers of length n, and n is a positive integer.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop will return False if any element in the list is not 0. If all elements in the list are 0, the loop will complete all iterations without returning, and the state of the list and n will remain unchanged.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts a list of integers and a positive integer `n` representing the length of the list. It checks if all elements in the list are 0. If any element is not 0, the function returns `False`. If all elements are 0, the function returns `True`. The state of the list and `n` remains unchanged.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that 3 <= n <= len(list).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: list[0] to list[n-2] are 0, and list[n-1] and beyond are unchanged.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *list[0] to list[n-2] are 0, and list[n-1] and beyond are unchanged. If `func_1(list, n)` returns `True`, the function `func_1` evaluated on `list` and `n` returns `True`. Otherwise, `func_1(list, n)` returns `False`.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` where 3 <= n <= len(list). It modifies the list such that elements from index 0 to index n-2 are set to 0, while elements from index n-1 onwards remain unchanged. The function then evaluates `func_1(list, n)` and prints 'YES' if `func_1` returns `True`, otherwise it prints 'NO'. The final state of the program is that the list has been modified as described, and the output is either 'YES' or 'NO' based on the evaluation of `func_1`.

