#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop does not modify the list or n. The loop will return False if any element in the list from index 0 to n-1 is non-zero. If all elements from index 0 to n-1 are zero, the loop will complete without returning False.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` where 0 <= n <= len(list). It checks if all elements in the list from index 0 to n-1 are zero. If any element is non-zero, the function returns `False`. If all elements from index 0 to n-1 are zero, the function returns `True`.

#State of the program right berfore the function call: list is a list of non-negative integers of length n, and n is an integer such that 3 <= n <= 2 * 10^5.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: The list is modified such that for each i in the range 1 to n-2, if the initial conditions (list[i] > 1, list[i - 1] > 0, and list[i + 1] > 0) were met, the values of list[i], list[i - 1], and list[i + 1] are decreased according to the operations inside the while loop. If at any point list[i - 1] becomes 0, the loop prints 'no' and returns, terminating the function. If the loop completes without list[i - 1] becoming 0 for any i, the list will have been modified but will not contain any 'no' print statements.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list is modified such that for each i in the range 1 to n-2, if the initial conditions (list[i] > 1, list[i - 1] > 0, and list[i + 1] > 0) were met, the values of list[i], list[i - 1], and list[i + 1] are decreased according to the operations inside the while loop. If at any point list[i - 1] becomes 0, the loop prints 'no' and returns, terminating the function. If the loop completes without list[i - 1] becoming 0 for any i, the list will have been modified but will not contain any 'no' print statements. Additionally, if `func_1(list, n)` returns `True`, the function indicates that the list and n satisfy the conditions checked by `func_1`. If `func_1(list, n)` returns `False`, the function indicates that the list and n do not satisfy these conditions.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` where 3 <= n <= 2 * 10^5. It modifies the list such that for each index `i` in the range 1 to n-2, if the conditions `list[i] > 1`, `list[i - 1] > 0`, and `list[i + 1] > 0` are met, the values at `list[i]`, `list[i - 1]`, and `list[i + 1]` are decreased according to specific operations. If at any point `list[i - 1]` becomes 0, the function prints 'no' and returns immediately. If the loop completes without any `list[i - 1]` becoming 0, the function calls `func_1(list, n)`. If `func_1(list, n)` returns `True`, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value explicitly.

