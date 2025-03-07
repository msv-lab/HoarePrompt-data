#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_j <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: After processing all test cases, `numTest` remains unchanged, `t` remains unchanged, `n` and `a` are modified for each test case based on the operations performed, and the output for each test case is either 'YES' or 'NO' printed to the console.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if a specific sequence of operations can reduce the last two elements of the list `a` to zero without any element becoming negative during the process. It prints 'YES' if it's possible, otherwise 'NO'.

