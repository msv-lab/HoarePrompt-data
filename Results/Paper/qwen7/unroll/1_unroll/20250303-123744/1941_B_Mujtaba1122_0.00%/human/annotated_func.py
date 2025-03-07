#State of the program right berfore the function call: list is a list of non-negative integers, and n is a positive integer representing the length of the list.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The list remains unchanged, and the function returns True if all elements in the list are zero; otherwise, it never returns (the loop completes without returning).
    return True
    #The program returns True if all elements in the list are zero; otherwise, it does not return anything.
#Overall this is what the function does:The function accepts a list of non-negative integers and a positive integer representing the length of the list. It checks if all elements in the list are zero. If all elements are zero, it returns True; otherwise, it does not return anything.

#State of the program right berfore the function call: `list` is a list of integers representing the array `a` of length `n`, where `3 <= n <= 2 \cdot 10^5` and `0 <= a_j \le 10^9`.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: Output State: The list will be such that for every element `list[i]` where `1 < i < n-1`, if `list[i]` was greater than 1 initially and both `list[i-1]` and `list[i+1]` were greater than 0, then `list[i]` will be reduced by twice the value of `list[i-1]`, `list[i-1]` will be reduced by its own value, and `list[i+1]` will be reduced by the value of `list[i-1]`. After all possible reductions, the elements that were originally 0 or less than or equal to 1 will remain unchanged.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: For every element `list[i]` where `1 < i < n-1`, if `list[i]` was initially greater than 1 and both `list[i-1]` and `list[i+1]` were greater than 0, then `list[i]` will be reduced by twice the value of `list[i-1]`, `list[i-1]` will be reduced by its own value, and `list[i+1]` will be reduced by the value of `list[i-1]`. If these conditions are not met, `list[i]`, `list[i-1]`, and `list[i+1]` will remain unchanged. After all possible reductions, the elements that were originally 0 or less than or equal to 1 will remain unchanged.
#Overall this is what the function does:The function accepts a list of integers and its length as parameters. It iterates through the list (excluding the first and last elements) and reduces certain elements based on specific conditions. After processing, it checks if all elements in the list are less than or equal to 18. If so, it prints 'YES'; otherwise, it prints 'NO'. The final state of the list is such that elements that were initially greater than 1 and had neighbors greater than 0 have been reduced according to specified rules, while other elements remain unchanged.

