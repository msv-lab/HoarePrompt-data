#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The function did not return False, and all elements from list[0] to list[n-1] are 0.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` checks if all elements from the start of the list up to the nth index are zero. It returns `False` if any of these elements are non-zero, and `True` if all of them are zero.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is a positive integer such that n >= 3 and n equals the length of the list.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: [0, 0, 0, 0, 0, 0, ...]
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list is initialized with all elements as 0. If `func_1(list, n)` returns `True`, then the condition in the if part is satisfied. Otherwise, if `func_1(list, n)` returns `False`, then the condition in the else part is satisfied.
#Overall this is what the function does:The function `func_2` processes a list of non-negative integers of length `n` (where `n` is at least 3) by modifying its elements based on specific conditions. If during this process any element at position `i-1` is not zero after a certain operation, it prints 'no' and terminates. Otherwise, it calls another function `func_1` with the modified list and `n`. Depending on the return value of `func_1`, it prints either 'YES' or 'NO'. The function does not return any value.

