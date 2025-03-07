#State of the program right berfore the function call: list is a list of integers and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: True
    return True
    #The program returns True
#Overall this is what the function does:The function checks if the first `n` elements of the provided list are all zeros. If any of these elements is not zero, it returns `False`. If all the first `n` elements are zeros, it returns `True`.

#State of the program right berfore the function call: list is a list of integers, and n is an integer such that 3 <= n <= 2 * 10^5 and len(list) == n.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: [1, 1, ..., 1, 0, 0, ..., 0]
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list consists of a sequence of 1s followed by a sequence of 0s. If `func_1(list, n)` evaluates to `True`, the condition for the if part is satisfied. If `func_1(list, n)` evaluates to `False`, the condition for the else part is satisfied.
#Overall this is what the function does:The function `func_2` processes a list of integers by modifying its elements based on specific rules. It checks if the list can be transformed into a sequence of 1s followed by 0s. If the transformation is possible, it prints 'YES'; otherwise, it prints 'no'. The function does not return any value.

