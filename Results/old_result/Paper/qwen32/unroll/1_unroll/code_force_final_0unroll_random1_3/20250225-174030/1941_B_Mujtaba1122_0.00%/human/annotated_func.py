#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: list is a list of integers where the first n elements are 0, and n is a non-negative integer such that 0 <= n <= len(list). The function returns True.
    return True
    #The program returns True
#Overall this is what the function does:The function checks if the first `n` elements of the list are all zeros and returns `True` if they are, otherwise it returns `False`.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is a positive integer such that n = len(list) and n >= 3.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: list[0] is unchanged, list[1] to list[n-2] are all 0, list[n-1] is unchanged.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `list[0]` is unchanged, `list[1]` to `list[n-2]` are all 0, `list[n-1]` is unchanged, and `func_1(list, n)` evaluates to either true or false.
#Overall this is what the function does:The function `func_2` takes a list of non-negative integers and its length `n` (where `n` is at least 3) as input. It modifies the list such that all elements from the second to the second-to-last become zero, while the first and last elements remain unchanged. It then checks a condition using `func_1` and prints 'YES' if the condition is true, otherwise 'NO'. The final state of the program is that the list has been modified as described, and either 'YES' or 'NO' has been printed.

