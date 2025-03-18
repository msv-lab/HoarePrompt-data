#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop will either return False if any of the first n elements in the list are non-zero, or it will complete all iterations without returning if all of the first n elements are zero. The list and n will remain unchanged.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` where `0 <= n <= len(list)`. It checks if all the first `n` elements in the list are zero. If any of these elements are non-zero, the function returns `False`. If all the first `n` elements are zero, the function returns `True`. The list and `n` remain unchanged after the function call.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is a non-negative integer such that 3 <= n <= len(list).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: list[0] to list[n-3] are all 0, and list[n-2] to the end of the list remain unchanged.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: list[0] to list[n-3] are all 0, and list[n-2] to the end of the list remain unchanged. The function `func_1(list, n)` returns `True` if the condition in the if part is met; otherwise, it returns `False`.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and a non-negative integer `n` where 3 <= n <= len(list). It modifies the list such that the elements from index 0 to n-3 are set to 0, while the elements from index n-2 to the end of the list remain unchanged. The function then calls `func_1` with the modified list and `n`. If `func_1` returns `True`, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

