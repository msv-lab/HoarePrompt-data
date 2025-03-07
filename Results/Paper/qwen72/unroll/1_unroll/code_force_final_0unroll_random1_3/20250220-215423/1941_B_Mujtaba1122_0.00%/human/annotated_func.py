#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop will either return False if any of the first n elements in the list are non-zero, or it will complete all iterations without returning if all the first n elements are zero. The list and n remain unchanged.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` where 0 <= n <= len(list). It checks if all the first `n` elements in the list are zero. If any of these elements are non-zero, the function returns `False`. If all the first `n` elements are zero, the function returns `True`. The list and the value of `n` remain unchanged after the function call.

#State of the program right berfore the function call: list is a list of integers with length n, and n is an integer such that 3 <= n <= 2 * 10^5.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: The list will be modified such that for every element `list[i]` where `1 <= i < n - 1`, if `list[i] > 1` and both `list[i - 1]` and `list[i + 1]` are greater than 0, then `list[i - 1]` will be set to 0, `list[i]` will be reduced by `2 * list[i - 1]` (which is 2 times its original value before being set to 0), and `list[i + 1]` will be reduced by `list[i - 1]` (which is its original value before being set to 0). This process will continue until either `list[i]` is no longer greater than 1, or `list[i - 1]` or `list[i + 1]` is no longer greater than 0. The first and last elements of the list, `list[0]` and `list[n - 1]`, will not be modified by the loop.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list will be modified such that for every element `list[i]` where `1 <= i < n - 1`, if `list[i] > 1` and both `list[i - 1]` and `list[i + 1]` are greater than 0, then `list[i - 1]` will be set to 0, `list[i]` will be reduced by `2 * list[i - 1]` (which is 2 times its original value before being set to 0), and `list[i + 1]` will be reduced by `list[i - 1]` (which is its original value before being set to 0). This process will continue until either `list[i]` is no longer greater than 1, or `list[i - 1]` or `list[i + 1]` is no longer greater than 0. The first and last elements of the list, `list[0]` and `list[n - 1]`, will not be modified by the loop. Additionally, if `func_1(list, n)` returns `True`, the function `func_1` has returned `True`. Otherwise, if `func_1(list, n)` returns `False`, the function `func_1` has returned `False`.
#Overall this is what the function does:The function `func_2` accepts a list of integers and an integer `n` where 3 <= n <= 2 * 10^5. It modifies the list such that for every element `list[i]` where `1 <= i < n - 1`, if `list[i] > 1` and both `list[i - 1]` and `list[i + 1]` are greater than 0, then `list[i - 1]` is set to 0, `list[i]` is reduced by `2 * list[i - 1]` (which is 2 times its original value before being set to 0), and `list[i + 1]` is reduced by `list[i - 1]` (which is its original value before being set to 0). This process continues for each `i` until either `list[i]` is no longer greater than 1, or `list[i - 1]` or `list[i + 1]` is no longer greater than 0. The first and last elements of the list, `list[0]` and `list[n - 1]`, are not modified. After the list is processed, the function calls `func_1(list, n)` and prints 'YES' if `func_1` returns `True`, otherwise it prints 'NO'. The function does not return any value.

