#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: list is a list of integers where all elements from index 0 to n-1 are 0, and n is a non-negative integer such that 0 <= n <= len(list).
    return True
    #The program returns True
#Overall this is what the function does:The function checks if all elements in the list from index 0 to n-1 are zero. If any element in this range is not zero, it returns False. Otherwise, it returns True.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that 3 <= n <= len(list).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: the list with elements at positions `i - 1`, `i`, and `i + 1` reduced according to the loop operations, with no early termination due to the `if` condition.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list with elements at positions `i - 1`, `i`, and `i + 1` is reduced according to the loop operations, with no early termination due to the `if` condition. Additionally, `func_1(list, n)` returns either `True` or `False`.
#Overall this is what the function does:The function `func_2` takes a list of non-negative integers and an integer `n` (where `3 <= n <= len(list)`). It modifies the list by reducing certain elements based on specific conditions. If any element at position `i - 1` is not zero after the modifications, it prints 'no' and returns. Otherwise, it prints 'YES' if `func_1(list, n)` returns `True`, or 'NO' if `func_1(list, n)` returns `False`.

