#State of the program right berfore the function call: list is a list of integers representing the array a, and n is the length of the array such that 3 <= n <= 2 \* 10^5.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The function completes all iterations without returning False, meaning that for every element in the list from index 0 to n-1, the value is 0. Therefore, the final state of the list remains unchanged, and the value of `i` is `n`, indicating that the loop has completed all its iterations. The variable `n` also remains as the original length of the list, and no other changes occur to the list elements.
    #
    #In simpler terms: After running through all iterations, the list contains only zeros, and the function does not return False, implying all elements were checked and found to be zero.
    return True
    #The program returns True, indicating that all elements in the list were found to be zero during the iterations. The list remains unchanged with all elements as zero, and the variable `i` is equal to `n`, which is the original length of the list.
#Overall this is what the function does:The function accepts a list of integers and its length n. It checks each element in the list to determine if all elements are zero. If any non-zero element is found, the function returns False immediately. If the function completes all iterations without finding any non-zero elements, it returns True. In both cases, the list remains unchanged, and the variable `i` is set to `n`, indicating the end of the iteration.

#State of the program right berfore the function call: `list` is a list of non-negative integers representing the array `a`, and `n` is an integer such that 3 <= n <= 2 * 10^5. Each element in the list is in the range [0, 10^9].
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: All elements in the list are less than or equal to 0.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: All elements in the list are less than or equal to 0. If `func_1(list, n)` returns True, the postcondition remains unchanged. If `func_1(list, n)` returns False, the postcondition also remains unchanged.
#Overall this is what the function does:The function accepts a list of non-negative integers and an integer `n`. It iterates through the list (excluding the first and last elements), and for each element, it checks if certain conditions are met. If the conditions are not met, it modifies the list by reducing the values of the current and previous elements. After the loop, it calls another function `func_1(list, n)`. Based on the result of `func_1`, it prints either 'YES' or 'NO'. Regardless of the outcome, the final state of the list is such that all its elements are less than or equal to 0. The function does not return any value.

