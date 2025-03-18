#State of the program right berfore the function call: list is a list of integers representing the array elements, and n is an integer representing the number of elements in the array.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to `n`, and the function has not returned False during any iteration. This implies that for every index `j` from 0 to `n-1`, `list[j]` is 0. If any `list[j]` was not 0 at any point, the function would have returned False earlier. Therefore, the final output state is that the entire list consists of zeros.
    return True
    #The program returns True, indicating that all elements in the list 'list' are 0.
#Overall this is what the function does:The function accepts a list of integers and an integer representing the number of elements in the list. It checks whether all elements in the list are zero. If any element is non-zero, it returns False immediately. If the loop completes without finding any non-zero elements, it returns True, indicating that all elements in the list are zero.

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
        
    #State: Output State: The list becomes a series of zeros, with the exception that `list[n-1]` will be -4 * (n-1) if it was initially set to a non-zero value, and all other elements will be 0. This is because the loop continuously modifies the elements as per the given conditions, eventually leaving only the first element (or the last one if we consider the reverse operation) with a negative value if it started with a non-zero value, and all others as zero.
    #
    #To break it down further:
    #- The loop starts by checking if `list[i] > 1` and both `list[i-1] > 0` and `list[i+1] > 0`.
    #- If these conditions are met, it performs the specified operations: subtracting `2 * list[i-1]` from `list[i]`, subtracting `list[i-1]` from `list[i+1]`, and subtracting `list[i-1]` from `list[i-1]`.
    #- These operations continue until either `list[i]` is no longer greater than 1 or `list[i-1]` or `list[i+1]` is no longer greater than 0.
    #- After all iterations, the list will consist of zeros except for the last non-zero element (which could be `list[0]` or `list[n-1]` depending on the initial conditions), which will be -4 * (n-1) if it was initially set to a non-zero value.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list becomes a series of zeros, with the exception that the last non-zero element (either `list[0]` or `list[n-1]`) will be -4 * (n-1) if it was initially set to a non-zero value, and all other elements will be 0.
#Overall this is what the function does:The function accepts a list of integers and an integer n. It processes the list by repeatedly modifying its elements based on specific conditions. After processing, the list becomes a series of zeros, with the exception that the last non-zero element (either `list[0]` or `list[n-1]`) will be -4 * (n-1) if it was initially set to a non-zero value. The function prints 'YES' if `func_1(list, n)` returns True, otherwise it prints 'NO'.

