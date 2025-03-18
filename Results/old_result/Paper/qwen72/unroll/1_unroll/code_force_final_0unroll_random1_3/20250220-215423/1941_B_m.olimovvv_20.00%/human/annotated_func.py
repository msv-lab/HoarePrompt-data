#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j is an integer such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The loop iterates `t` times. For each iteration, it reads an integer `a` and a list of `n` integers `b`. If the first element of `b` is odd and not equal to the second element minus 2, or if the last element of `b` is odd and not equal to the second-to-last element minus 2, it prints 'NO'. Otherwise, it prints 'YES'. The values of `t`, `n`, and `a` are unchanged after the loop, and the list `a` remains the same as it was before the loop started.
#Overall this is what the function does:The function processes `t` test cases, where each test case involves reading an integer `a` and a list `b` of `a` integers. For each test case, it checks if the first element of `b` is odd and not equal to the second element minus 2, or if the last element of `b` is odd and not equal to the second-to-last element minus 2. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value. The values of `t` and `a` are unchanged after the function concludes, and the list `b` is redefined for each test case.

