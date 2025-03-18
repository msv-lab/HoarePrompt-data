#State of the program right berfore the function call: t is a positive integer, and for each test case, n is an integer such that 3 ≤ n ≤ 2 \* 10^5. The array a is a list of n integers where each integer a_j satisfies 0 ≤ a_j ≤ 10^9. The sum of all n values across all test cases does not exceed 2 \* 10^5.
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
        
    #State: Output State: After executing the loop for all test cases, for each test case, the array `a` will be modified according to the operations defined within the loop. If at any point a negative number is encountered in the array `a`, the program will immediately print 'NO' and stop further processing for that test case. If the loop completes without encountering a negative number and the last two elements of the array `a` are both zero, the program will print 'YES'. Otherwise, it will print 'NO'. The final state of the array `a` will reflect these operations, and the output will consist of either 'YES' or 'NO' for each test case.
#Overall this is what the function does:The function processes multiple test cases, each involving an array of integers `a` of length `n` (where `3 ≤ n ≤ 2 * 10^5`). For each test case, it checks if any element in the array `a` becomes negative after performing specific operations on consecutive elements. If any element becomes negative, it prints 'NO' and stops further processing for that test case. If the array passes all checks (i.e., no negative elements and the last two elements are zero), it prints 'YES'. Otherwise, it prints 'NO'. The function does not return a value but prints 'YES' or 'NO' for each test case.

