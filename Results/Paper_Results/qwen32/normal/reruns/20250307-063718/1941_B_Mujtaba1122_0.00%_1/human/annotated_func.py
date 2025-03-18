#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop has finished executing all iterations, and if none of the elements at indices from 0 to `n-1` in the list are non-zero, then the function has not returned False and the loop completes normally.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` checks if all elements in the list from index 0 to `n-1` are zero. It returns `False` if any of these elements are non-zero, and `True` if all of them are zero.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that 3 <= n <= len(list).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: The first `n-2` elements of the list are `0`, and the remaining elements remain unchanged.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The first `n-2` elements of the list are `0`, and the remaining elements remain unchanged. The function `func_1(list, n)` returns either `True` or `False`.
#Overall this is what the function does:The function `func_2` modifies the first `n-2` elements of the input list to `0` by performing a series of operations, then checks a condition using `func_1` and prints 'YES' or 'NO' based on the result. The remaining elements of the list beyond the `n-2` index remain unchanged.

