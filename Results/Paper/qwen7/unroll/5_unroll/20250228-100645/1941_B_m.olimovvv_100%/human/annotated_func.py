#State of the program right berfore the function call: t is a positive integer, and for each test case, n is an integer such that 3 ≤ n ≤ 2 \* 10^5. The array a consists of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j, and the sum of the values of n over all test cases does not exceed 2 \* 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: Output State: t is a positive integer, and for each test case, n is an integer such that 3 ≤ n ≤ 2 * 10^5. The array a consists of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j, and after executing the loop, if the conditions inside the loop are met for all elements, the last two elements of the array b are 0, otherwise, 'NO' is printed at some point during the loop execution. The sum of the values of n over all test cases does not exceed 2 * 10^5.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it checks if certain conditions are met by modifying the array \( b \) derived from \( a \). If any condition fails, it prints 'NO'. If all conditions are met for all elements, it prints 'YES'. The function does not return a value but prints 'YES' or 'NO' for each test case.

