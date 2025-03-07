#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list). The loop has completed all iterations without returning False.
    return True
    #The program returns True
#Overall this is what the function does:The function checks if the first `n` elements of the input list are all zeros and returns `True` if they are, otherwise it returns `False`.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is a non-negative integer such that 3 <= n <= len(list).
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: list with elements at positions i-1 set to 0 where conditions are met, and adjacent elements potentially reduced.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list has elements at positions i-1 set to 0 where conditions are met, and adjacent elements potentially reduced. Additionally, `func_1(list, n)` evaluates to either True or False.
#Overall this is what the function does:The function `func_2` modifies a list of non-negative integers by reducing certain elements based on specific conditions and then checks a condition using `func_1`. It prints 'YES' if `func_1` returns True, otherwise it prints 'NO'. The final state of the program includes a potentially modified list and a printed message indicating the result of the check.

