#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j satisfies 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The value of `numTest` is decremented by the number of iterations completed. The values of `n` and `a` are updated for each iteration based on the input provided during that iteration. The variables `t` and `n` retain their initial values after the loop completes, but the list `a` will be modified according to the operations performed within the loop. The variable `stop` is reset to `False` at the beginning of each iteration.
#Overall this is what the function does:The function `func` reads a series of test cases from the input. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then performs a series of operations on the list `a` and checks if the last two elements of `a` can be reduced to zero by these operations without any element in `a` becoming negative. If the conditions are met, it prints 'YES' for that test case; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case. After processing all test cases, the function concludes, and the input variables `t`, `n`, and `a` are no longer relevant as they are re-read for each test case.

