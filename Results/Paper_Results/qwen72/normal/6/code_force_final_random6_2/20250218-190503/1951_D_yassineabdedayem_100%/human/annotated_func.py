#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers where 1 ≤ n, k ≤ 10^18.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: `t` is an input integer where 0 ≤ t ≤ 1000, `_` is a placeholder variable, `n` and `k` are positive integers where 1 ≤ n, k ≤ 10^18. For each test case, if `n` is equal to `k`, then `n` is equal to `k`. If `n` is not equal to `k` and `n + 2` is greater than `k * 2`, then `n + 2` is greater than `k * 2`. If `n` is not equal to `k` and `n + 2` is less than or equal to `k * 2`, then `n + 2` is less than or equal to `k * 2`.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 1000) indicating the number of test cases. For each test case, it reads two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18). The function then checks the following conditions for each test case:
- If `n` is equal to `k`, it prints 'YES' followed by two lines, each containing the number 1.
- If `n + 2` is greater than `k * 2`, it prints 'YES' followed by two lines: the first line contains the number 2, and the second line contains the values `n - k + 1` and 1.
- If neither of the above conditions is met, it prints 'NO'. After processing all test cases, the function completes execution.

