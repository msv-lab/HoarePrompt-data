#State of the program right berfore the function call: list is a list of integers representing the array elements, and n is an integer representing the number of elements in the array.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The list remains unchanged, and the value of n remains unchanged. If any element in the list is not 0, the loop will return False; otherwise, it will return True after completing all iterations.
    return True
    #The program returns True if all elements in the list are 0, otherwise it returns False.
#Overall this is what the function does:The function accepts a list of integers and an integer representing the number of elements in the list. It checks whether all elements in the list are zero. If any element is non-zero, it immediately returns False. If all elements are zero, it returns True. The function does not modify the original list or the value of n.

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
        
    #State: Output State: The list `list` undergoes modifications based on the conditions within the loop. For each `i` from 1 to `n-2`, if `list[i] > 1` and both `list[i-1] > 0` and `list[i+1] > 0`, then `list[i+1]` is decreased by `list[i-1]`, `list[i]` is decreased by `2 * list[i-1]`, and `list[i-1]` is decreased by `list[i-1]`. If at any point `list[i-1]` is not zero, the program prints 'no' and returns immediately. After all iterations, if no early termination occurs, the final state of the list `list` is the result of these operations.
    #
    #If the loop completes without printing 'no', the output state will be a modified version of the initial list where each element has been adjusted according to the specified rules.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list `list` undergoes modifications based on the conditions within the loop. For each `i` from 1 to `n-2`, if `list[i] > 1` and both `list[i-1] > 0` and `list[i+1] > 0`, then `list[i+1]` is decreased by `list[i-1]`, `list[i]` is decreased by `2 * list[i-1]`, and `list[i-1]` is decreased by `list[i-1]`. If at any point `list[i-1]` is not zero, the program prints 'no' and returns immediately. After all iterations, if no early termination occurs, the final state of the list `list` is the result of these operations. Regardless of whether `func_1(list, n)` evaluates to True or False, the final state of the list remains consistent with the described operations.
#Overall this is what the function does:The function accepts a list of integers and an integer n. It iterates through the list, modifying its elements based on specific conditions. If any condition is violated during the iteration, it prints 'no' and returns immediately. If the iteration completes without violating any conditions, it calls another function `func_1(list, n)`. Based on the result of `func_1`, it prints either 'YES' or 'NO'. Regardless of the outcome, the final state of the list reflects the modifications performed during the iteration.

