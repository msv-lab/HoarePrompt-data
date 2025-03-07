#State of the program right berfore the function call: list is a list of integers representing the array elements, and n is an integer representing the number of elements in the array.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The list remains unchanged, and the value of n remains unchanged. If any element in the list is 0, the loop will return False, otherwise, it will complete all iterations without returning, implying all elements are non-zero.
    return True
    #The program returns True, indicating that all elements in the list are non-zero.
#Overall this is what the function does:The function accepts a list of integers and an integer representing the number of elements in the list. It checks whether all elements in the list are non-zero. If any element is zero, the function returns False immediately. Otherwise, it completes its execution and returns True, indicating that all elements in the list are non-zero.

#State of the program right berfore the function call: list is a list of integers representing the array a, and n is an integer such that 3 <= n <= 2 \* 10^5.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: Output State: The list has been modified according to the rules inside the loop. For each element `list[i]` where `1 <= i <= n-2`, if `list[i] > 1` and both `list[i-1] > 0` and `list[i+1] > 0`, then `list[i]` is decreased by twice the value of `list[i-1]`, `list[i+1]` is decreased by the value of `list[i-1]`, and `list[i-1]` is decreased by itself (effectively setting it to 0). If at any point during these operations `list[i-1]` is not zero, the program prints 'no' and returns immediately. If the loop completes without printing 'no', the final state of the list is the result of all these operations.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list has been modified according to the rules inside the loop. For each element `list[i]` where `1 <= i <= n-2`, if `list[i] > 1` and both `list[i-1] > 0` and `list[i+1] > 0`, then `list[i]` is decreased by twice the value of `list[i-1]`, `list[i+1]` is decreased by the value of `list[i-1]`, and `list[i-1]` is decreased by itself (effectively setting it to 0). If at any point during these operations `list[i-1]` is not zero, the program prints 'no' and returns immediately. If the loop completes without printing 'no', the final state of the list is the result of all these operations. This outcome is the same regardless of whether `func_1(list, n)` returns `True` or `False`.
#Overall this is what the function does:The function accepts a list of integers and an integer n. It modifies the list according to specific rules within a loop. For each element `list[i]` where `1 <= i <= n-2`, if `list[i] > 1` and both `list[i-1] > 0` and `list[i+1] > 0`, then `list[i]` is decreased by twice the value of `list[i-1]`, `list[i+1]` is decreased by the value of `list[i-1]`, and `list[i-1]` is decreased by itself (effectively setting it to 0). If at any point during these operations `list[i-1]` is not zero, the function prints 'no' and returns immediately. If the loop completes without printing 'no', the function calls `func_1(list, n)`. Based on the result of `func_1`, the function prints either 'YES' or 'NO'. The final state of the list is the result of all these operations.

