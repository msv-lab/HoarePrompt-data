#State of the program right berfore the function call: list is a list of integers, and n is a non-negative integer such that 0 <= n <= len(list).
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: the loop has finished all iterations without returning False, meaning all elements from index 0 to n-1 are 0.
    return True
    #The program returns True
#Overall this is what the function does:The function checks if all elements in the list from index 0 to n-1 are zero. It returns True if they are all zero, otherwise it returns False.

#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer such that 3 <= n <= 2 * 10^5 and n is equal to the length of the list.
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: the list will have been modified such that elements from index 1 to n-2 may be reduced to 0 or some other values based on initial list configuration, and the first and last elements will remain unchanged unless they were part of the reduction operations.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list will have been modified such that elements from index 1 to n-2 may be reduced to 0 or some other values based on the initial list configuration, and the first and last elements will remain unchanged unless they were part of the reduction operations. Additionally, the function `func_1(list, n)` will have been evaluated, and its result (either True or False) will be known.
#Overall this is what the function does:The function `func_2` takes a list of non-negative integers and an integer `n` as input, where `n` is the length of the list and is between 3 and 2 * 10^5. It modifies the list by potentially reducing the values of elements from index 1 to `n-2` based on the values of their neighboring elements. After modifying the list, it checks a condition using another function `func_1`. If the condition is met, it prints "YES"; otherwise, it prints "NO". The final state of the program involves the list being potentially modified and a printed message indicating whether the condition was met.

