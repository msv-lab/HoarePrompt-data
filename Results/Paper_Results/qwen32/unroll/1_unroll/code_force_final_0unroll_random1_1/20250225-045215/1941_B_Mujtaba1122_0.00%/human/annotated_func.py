#State of the program right berfore the function call: list is a list of non-negative integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: the loop has finished executing without returning False.
    return True
    #The program returns True
#Overall this is what the function does:The function checks if the first `n` elements of the list are all zeros. It returns `True` if they are, and `False` otherwise.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that 3 <= n <= len(list).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: list = [0, 0, ..., 0, list[n-1], list[n], ..., list[len(list)-1]]
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list is structured such that the first `n` elements are all 0, and the remaining elements are integers. The function `func_1` returns `True` if the list and `n` meet a specific condition, otherwise it returns `False`.
#Overall this is what the function does:The function `func_2` modifies the first `n-2` elements of the input list to zero under certain conditions and then checks if the modified list and `n` satisfy a specific condition using the function `func_1`. It prints 'YES' if `func_1` returns `True`, otherwise it prints 'NO'. The final state of the program is that the first `n` elements of the list are zero, and the remaining elements are integers.

