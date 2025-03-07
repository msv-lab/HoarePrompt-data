#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j is an integer such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 3 <= n <= 2 * 10^5, `a` is a list of `n` integers where each element `a_j` is an integer such that 0 <= a_j <= 10^9, the sum of the values of `n` over all test cases does not exceed 2 * 10^5, `b` is a list of integers input by the user, `i` is `n - 3`, `b[0]` to `b[n-3]` are all 0, `b[n-2]` is `b[n-2] - 2 * b[n-3]`, and `b[n-1]` is `b[n-1] - b[n-3]`. If any element in `b` from `b[0]` to `b[n-2]` was less than 0 during the loop, the loop would have terminated early with a 'NO' output. If `b[n-1]` or `b[n-2]` are not 0 after the loop, the output will be 'NO'. Otherwise, the output will be 'YES'.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` and a list `b` of `n` integers. For each test case, it modifies the elements of `b` according to a specific rule and checks if the final state of `b` meets certain conditions. If any element in `b` becomes negative during the modification process, or if the last two elements of `b` are not zero after the process, the function outputs 'NO' for that test case. Otherwise, it outputs 'YES'. The function does not return any value.

