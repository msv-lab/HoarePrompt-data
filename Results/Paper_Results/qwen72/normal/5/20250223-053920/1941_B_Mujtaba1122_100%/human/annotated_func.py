#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: The loop does not modify the list or n. The loop checks each element in the list from index 0 to n-1. If any element is not 0, the loop immediately returns False. If the loop completes all iterations without finding any non-zero elements, it does not return anything explicitly, so the function will return None.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts a list of integers `list` and a non-negative integer `n` where `0 <= n <= len(list)`. It checks if all elements in the list from index 0 to index `n-1` are zero. If any element is non-zero, the function returns `False`. If all elements are zero or if `n` is 0, the function returns `True`.

#State of the program right berfore the function call: list is a list of integers with length n, and n is an integer such that 3 <= n <= 2 * 10^5.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: The list will be modified such that all elements from index 1 to index \(n-2\) will be zero, and the first element (`list[0]`) and the last element (`list[n-1]`) will remain unchanged. If the loop encounters a non-zero `list[i - 1]` after the inner loop, it will print 'no' and terminate.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list will be modified such that all elements from index 1 to index \(n-2\) will be zero, and the first element (`list[0]`) and the last element (`list[n-1]`) will remain unchanged. If `func_1(list, n)` returns `True`, it indicates that the condition inside `func_1` has been met. If `func_1(list, n)` returns `False`, it indicates that the condition inside `func_1` has not been met.
#Overall this is what the function does:The function `func_2` accepts a list of integers and an integer `n` where 3 <= n <= 2 * 10^5. It modifies the list such that all elements from index 1 to index \(n-2\) are set to zero, while the first element (`list[0]`) and the last element (`list[n-1]`) remain unchanged. If at any point during the modification process, an element at index \(i-1\) is found to be non-zero, the function prints 'no' and returns immediately. If the list is successfully modified and `func_1(list, n)` returns `True`, the function prints 'YES'. If `func_1(list, n)` returns `False`, the function prints 'NO'.

