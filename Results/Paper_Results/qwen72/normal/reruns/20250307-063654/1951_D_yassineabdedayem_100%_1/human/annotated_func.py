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
        
    #State: `t` is an input integer where 1 ≤ t ≤ 1000, and for each test case, `n` and `k` are positive integers where 1 ≤ n, k ≤ 10^18. The loop has executed `t` times, and for each iteration, if `n` was equal to `k`, 'YES' and two 1s were printed. If `n` was not equal to `k` and `n + 2` was greater than `k * 2`, 'YES' and the values `n - k + 1` and 1 were printed. If `n + 2` was less than or equal to `k * 2`, 'NO' was printed. After all iterations, `t` is 0.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases (1 ≤ t ≤ 1000). For each test case, it reads two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18). It then checks the following conditions for each test case:
- If `n` is equal to `k`, it prints 'YES' followed by two 1s.
- If `n + 2` is greater than `k * 2`, it prints 'YES' followed by `n - k + 1` and 1.
- If neither of the above conditions is true, it prints 'NO'.
After processing all `t` test cases, the function completes without returning any value. The final state is that `t` test cases have been processed, and the appropriate output has been printed for each case.

