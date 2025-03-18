#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9; the sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: numTest is an input integer, and all other variables are in their initial state. After executing the loop, for each test case, if any element in the array `a` is negative before the inner loop ends, it prints 'NO' and stops further processing for that test case. If the last two elements of the array `a` are not zero after the inner loop, it also prints 'NO'. Otherwise, it prints 'YES'. All other variables remain unchanged.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t (number of test cases), an integer n (size of the array), and an array a of n integers. It then iterates through the array and modifies its elements according to specific rules. If any element becomes negative during the iteration, it prints 'NO' and stops further processing for that test case. If the last two elements of the array are not zero after the iteration, it also prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.

