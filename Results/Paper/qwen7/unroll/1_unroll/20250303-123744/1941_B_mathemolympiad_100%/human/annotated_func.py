#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j in the array. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: After executing the loop for all test cases, for each test case, if there exists any negative value in the array `a` before the end of the array (i.e., indices from 0 to n-3), the program prints 'NO' for that test case and moves to the next test case. If no negative values are found and the last two elements of the array are zero, the program prints 'YES' for that test case; otherwise, it prints 'NO'. All other variables and their states remain unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and an array `a` of size `n`. It then iterates through the array, modifying its values based on the first element of each segment of three consecutive elements. If any element in the array becomes negative before reaching the second-to-last element, the function prints 'NO' for that test case and moves to the next one. If the function completes the iteration without finding any negative elements and the last two elements of the array are zero, it prints 'YES' for that test case; otherwise, it prints 'NO'. The function does not return any value but prints 'YES' or 'NO' for each test case.

