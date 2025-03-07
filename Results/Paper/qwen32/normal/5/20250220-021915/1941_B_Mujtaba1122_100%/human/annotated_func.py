#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop has completed all `n` iterations without returning `False`, indicating that all elements in `list` from index 0 to `n-1` are 0. The function will implicitly return `None`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` checks if the first `n` elements of the input list are all zeros. It returns `False` if any of these elements are not zero, and `True` if all of them are zero.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that n >= 3 and n is equal to the length of list.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: [0, 0, 0]
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list remains `[0, 0, 0]`. If `func_1(list, n)` evaluates to True, the current state of the program includes these conditions being satisfied. Otherwise, the condition checked by `func_1(list, n)` is false.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` representing the length of the list, which must be at least 3. It modifies the list in place and prints either 'no', 'YES', or 'NO' based on certain conditions. The function does not return any value (returns `None`).

