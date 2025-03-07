#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop does not modify the list or n. The loop will return False if any element in the list from index 0 to n-1 is not 0. If all elements from index 0 to n-1 are 0, the loop will complete without returning, and the program will continue executing the next line of code.
    return True
    #The program returns True if all elements from index 0 to n-1 in the list are 0. If any element in the list from index 0 to n-1 is not 0, the program returns False.
#Overall this is what the function does:The function `func_1` accepts a list of integers and a non-negative integer `n` (where 0 <= n <= len(list)). It returns `True` if all elements from index 0 to n-1 in the list are 0. If any element in this range is not 0, it returns `False`. The function does not modify the input list or the value of `n`.

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
        
    #State: The list will have zeros at all positions from 0 to n-2, and the elements at positions 1 to n-2 will be reduced by twice the original value of their preceding element, while the elements at positions 2 to n-1 will be reduced by the original value of their preceding element.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list will have zeros at all positions from 0 to n-2, and the elements at positions 1 to n-2 will be reduced by twice the original value of their preceding element, while the elements at positions 2 to n-1 will be reduced by the original value of their preceding element. Additionally, the function `func_1(list, n)` will return `True` if the current state of the list and the value of `n` satisfy the condition within `func_1`, otherwise it will return `False`.
#Overall this is what the function does:The function `func_2` accepts a list of non-negative integers and an integer `n` where 3 <= n <= len(list). It modifies the list such that all elements from index 0 to n-2 are set to zero. The function returns `None` but prints 'no' and exits early if any element from index 0 to n-2 is not zero after the modification process. If the modification process completes and all elements from index 0 to n-2 are zero, the function calls `func_1(list, n)` and prints 'YES' if `func_1` returns `True`, otherwise it prints 'NO'.

