#State of the program right berfore the function call: list is a list of non-negative integers, and n is a positive integer such that n is the length of the list.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The list remains unchanged, and the function returns `True`. This means that all elements in the list are non-zero.
    return True
    #The program returns True, indicating that all elements in the list are non-zero.
#Overall this is what the function does:The function accepts a list of non-negative integers and a positive integer representing the length of the list. It checks whether all elements in the list are non-zero. If all elements are non-zero, it returns True; otherwise, it returns False before even reaching the return statement due to encountering a zero element.

#State of the program right berfore the function call: `list` is a list of integers representing the array `a`, and `n` is an integer such that 3 <= n <= 2 * 10^5. Each element in the list is an integer in the range [0, 10^9].
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: Output State: The list `list` will be modified according to the operations inside the loop. For each `i` from 1 to `n-2`, if `list[i] > 1` and both `list[i-1]` and `list[i+1]` are greater than 0, the value of `list[i]` is decreased by twice the value of `list[i-1]`, the value of `list[i+1]` is decreased by the value of `list[i-1]`, and the value of `list[i-1]` is decreased by itself (effectively halved). If at any point `list[i-1]` is not zero during the execution of the loop, the program prints 'no' and returns immediately, meaning the loop does not complete all iterations. If the loop completes without printing 'no', the final state of the list `list` will be the result of all the operations performed within the loop.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list `list` will be modified according to the operations inside the loop. For each `i` from 1 to `n-2`, if `list[i] > 1` and both `list[i-1]` and `list[i+1]` are greater than 0, the value of `list[i]` is decreased by twice the value of `list[i-1]`, the value of `list[i+1]` is decreased by the value of `list[i-1]`, and the value of `list[i-1]` is decreased by itself (effectively halved). If at any point `list[i-1]` is not zero during the execution of the loop, the program prints 'no' and returns immediately, meaning the loop does not complete all iterations. If the loop completes without printing 'no', the final state of the list `list` will be the result of all the operations performed within the loop. The function `func_1(list, n)` determines whether the loop completes without printing 'no', returning `True` if it does and `False` otherwise.
#Overall this is what the function does:The function accepts a list of integers and an integer n. It modifies the list according to specific rules within a loop. For each index i from 1 to n-2, if the element at index i is greater than 1 and the elements at indices i-1 and i+1 are greater than 0, it decreases the element at index i by twice the value of the element at index i-1, decreases the element at index i+1 by the value of the element at index i-1, and decreases the element at index i-1 by itself (effectively halving it). If at any point the element at index i-1 is not zero, it prints 'no' and returns immediately. If the loop completes without printing 'no', it calls another function `func_1(list, n)`. Based on the result of `func_1`, it prints either 'YES' or 'NO'. The final state of the list is the result of all the operations performed within the loop.

