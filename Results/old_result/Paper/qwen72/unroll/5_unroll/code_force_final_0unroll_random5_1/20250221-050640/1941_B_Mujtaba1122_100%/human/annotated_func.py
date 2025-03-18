#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop has completed all iterations, and the list and n remain unchanged. If any element in the list from index 0 to n-1 is non-zero, the function returns False. If all elements in the list from index 0 to n-1 are zero, the function does not return False and continues execution after the loop.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` (where 0 <= n <= len(list)). It checks if all elements in the list from index 0 to n-1 are zero. If any element is non-zero, the function returns `False`. If all elements are zero, the function returns `True`.

#State of the program right berfore the function call: list is a list of integers of length n, and n is an integer such that 3 <= n <= 2 * 10^5. All elements in list are non-negative integers (0 <= a_j <= 10^9).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: The list is modified such that for each index i (1 <= i < n - 1), if list[i] was initially greater than 1 and both list[i - 1] and list[i + 1] were greater than 0, then list[i] and list[i - 1] are reduced to 0, and list[i + 1] is reduced by the value of list[i - 1]. If at any point list[i - 1] is not 0, the loop prints 'no' and returns, leaving the list in an undefined state. Otherwise, the loop completes and the list is in a state where no index i (1 <= i < n - 1) has list[i] > 1 and both list[i - 1] > 0 and list[i + 1] > 0.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list is modified such that for each index i (1 <= i < n - 1), if list[i] was initially greater than 1 and both list[i - 1] and list[i + 1] were greater than 0, then list[i] and list[i - 1] are reduced to 0, and list[i + 1] is reduced by the value of list[i - 1]. If at any point list[i - 1] is not 0, the loop prints 'no' and returns, leaving the list in an undefined state. Otherwise, the loop completes and the list is in a state where no index i (1 <= i < n - 1) has list[i] > 1 and both list[i - 1] > 0 and list[i + 1] > 0. Additionally, the function `func_1(list, n)` either returns `True` or `False`, which determines whether the if or else part was executed.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` where 3 <= n <= 2 * 10^5. It modifies the list such that for each index `i` (1 <= i < n - 1), if `list[i]` is greater than 1 and both `list[i - 1]` and `list[i + 1]` are greater than 0, then `list[i]` and `list[i - 1]` are reduced to 0, and `list[i + 1]` is reduced by the value of `list[i - 1]`. If at any point `list[i - 1]` is not 0, the function prints 'no' and returns, leaving the list in an undefined state. If the loop completes without encountering this condition, the function calls `func_1(list, n)`. If `func_1(list, n)` returns `True`, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

