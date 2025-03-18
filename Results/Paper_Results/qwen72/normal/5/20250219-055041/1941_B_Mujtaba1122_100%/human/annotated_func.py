#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: `list` is a list of integers, `n` is a non-negative integer such that 0 <= n <= len(list), and `i` is `n-1`. If any element in the first `n` elements of `list` is not 0, the function returns False. Otherwise, all the first `n` elements of `list` are 0.
    return True
    #The program returns True, indicating that all the first `n` elements in the list `list` are 0, where `n` is a non-negative integer such that 0 <= n <= len(list), and `i` is `n-1`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` (where 0 <= n <= len(list)). It returns `False` if any of the first `n` elements in the list are not 0. If all the first `n` elements are 0, it returns `True`.

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
        
    #State: The list is a list of non-negative integers of length `n` (3 <= n <= 2 * 10^5), `i` is `n-1`, `list[0]` is 0, `list[1]` is 0, and for all `j` in the range `2` to `n-2`, `list[j]` is 0. The value of `list[n-1]` is the original value of `list[n-1]` minus the sum of all the values that were originally in `list[2]` to `list[n-2]` multiplied by 1, and `list[n-2]` is 0.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list is a list of non-negative integers of length `n` (3 <= n <= 2 * 10^5), `i` is `n-1`, `list[0]` is 0, `list[1]` is 0, and for all `j` in the range `2` to `n-2`, `list[j]` is 0. The value of `list[n-1]` is the original value of `list[n-1]` minus the sum of all the values that were originally in `list[2]` to `list[n-2]` multiplied by 1, and `list[n-2]` is 0. If `func_1(list, n)` returns `True`, the function returns `True`. Otherwise, if `func_1(list, n)` returns `False`, the function returns `False`.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` within the range 3 to 200,000. It modifies the list such that, after execution, the first two elements (`list[0]` and `list[1]`) are 0, and all elements from index 2 to `n-2` are also 0. The last element (`list[n-1]`) is reduced by the sum of the original values from index 2 to `n-2`. The function then calls another function `func_1` with the modified list and `n`. If `func_1` returns `True`, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

