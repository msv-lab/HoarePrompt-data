#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
    return True
    #The program returns True
#Overall this is what the function does:The function checks if the first `n` elements of the input list are all zeros. If any of these elements is not zero, it returns `False`. Otherwise, it returns `True`.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that 3 <= n <= 2 * 10^5 and n is equal to the length of list.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: The list will have modified values with many elements potentially reduced to 0, and some elements adjusted based on the reductions. The exact state depends on the initial values of the list.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list will have modified values with many elements potentially reduced to 0, and some elements adjusted based on the reductions. The exact state depends on the initial values of the list. The function `func_1(list, n)` is evaluated, and it can either return True or False.
#Overall this is what the function does:The function `func_2` modifies a list of non-negative integers by reducing certain elements based on specific conditions. It prints 'no' if any element at position `i-1` is not zero after a series of adjustments. If all elements at position `i-1` are zero, it calls another function `func_1` to determine if the final state of the list meets a certain condition, printing 'YES' if true and 'NO' if false. The final state of the program depends on the initial values of the list and the outcome of `func_1`.

