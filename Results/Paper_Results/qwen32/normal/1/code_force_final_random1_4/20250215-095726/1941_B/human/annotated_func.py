#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 3 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_j satisfies 0 ≤ a_j ≤ 10^9. The sum of all n values across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The loop will have executed `t` times, where `t` is the initial integer input. For each of these `t` executions, the program will have read an integer `a` and a list of integers `b`. It will have printed 'NO' if the first element of `b` is odd and the second element is not equal to the first element plus 2, or if the last element of `b` is odd and the second-to-last element is not equal to the last element plus 2. Otherwise, it will have printed 'YES'. The values of `t`, `a`, and `b` will be reset for each iteration but will not persist beyond the current iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `b` of `n` integers. For each test case, it checks if the first element of `b` is odd and not equal to the second element plus 2, or if the last element of `b` is odd and not equal to the second-to-last element plus 2. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'.

