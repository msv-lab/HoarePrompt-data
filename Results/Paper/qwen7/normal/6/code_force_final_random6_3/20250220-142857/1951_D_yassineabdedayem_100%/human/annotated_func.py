#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
        
    #State: The variable `t` will be an integer such that \(1 \leq t \leq 1000\), `n` will be the minimum value between the original `n` and \(2 * k - 2\), and `k` will be the last integer read from standard input during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers: t, n, and k. For each test case, it determines whether a certain condition is met and prints 'YES' or 'NO' accordingly. If the condition is met, it also prints two additional integers. The function reads these values from standard input and does not return any value.

