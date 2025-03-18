#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j is such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func():
    numTest = int(input())
    for _ in range(0, numTest):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        stop = False
        
        for i in range(0, n - 2):
            if a[i] < 0:
                print('NO')
                stop = True
                break
            opNum = a[i]
            a[i] -= opNum
            a[i + 1] -= 2 * opNum
            a[i + 2] -= opNum
        
        if stop == True:
            continue
        
        if a[len(a) - 1] != 0 or a[len(a) - 2] != 0:
            print('NO')
        else:
            print('YES')
        
    #State: The values of `t`, `n`, and `a` remain unchanged, but the loop will have printed 'NO' or 'YES' for each test case based on the conditions inside the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then checks if the list `a` can be modified through a series of operations such that the last two elements of the list become zero. If at any point an element in the list is negative, or if the last two elements are not zero after the operations, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value and does not modify the input variables `t`, `n`, or `a` outside the scope of the loop.

