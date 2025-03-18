#State of the program right berfore the function call: list is a list of integers, n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop will either return False if any element in the list from index 0 to n-1 is non-zero, or it will complete all iterations without returning if all elements in this range are zero. The list and n remain unchanged.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` where `0 <= n <= len(list)`. It checks if all elements in the list from index 0 to n-1 are zero. If any element in this range is non-zero, the function returns `False`. If all elements in this range are zero, the function returns `True`. The list and the value of `n` remain unchanged.

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
        
    #State: list[i - 1] is 0 for all i in the range 1 to n - 2, list[i] is 1 or less for all i in the range 1 to n - 2, and list[i + 1] is reduced by the cumulative value of list[i - 1] for all i in the range 1 to n - 2.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: list[i - 1] is 0 for all i in the range 1 to n - 2, list[i] is 1 or less for all i in the range 1 to n - 2, and list[i + 1] is reduced by the cumulative value of list[i - 1] for all i in the range 1 to n - 2. If `func_1(list, n)` returns `True`, the function returns `True`. Otherwise, the function returns `False`.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` where 3 <= n <= len(list). It modifies the list such that for each index `i` in the range 1 to n-2, the elements at `list[i-1]`, `list[i]`, and `list[i+1]` are reduced based on the values of `list[i-1]` and the conditions specified. If at any point `list[i-1]` is not zero, the function prints 'no' and returns `None`. If the function completes the loop without early termination, it calls `func_1(list, n)`. If `func_1(list, n)` returns `True`, the function prints 'YES' and returns `True`; otherwise, it prints 'NO' and returns `False`. The final state of the list is such that `list[i-1]` is 0 for all `i` in the range 1 to n-2, `list[i]` is 1 or less for all `i` in the range 1 to n-2, and `list[i+1]` is reduced by the cumulative value of `list[i-1]` for all `i` in the range 1 to n-2.

