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
        
    #State: Output State: The value of `t` is an integer between 1 and 1000. For each iteration of the loop, based on the values of `n` and `k`:
    #- If `n` equals `k`, the output will be 'YES', followed by 1 and 1.
    #- If `n + 2` is greater than `k * 2`, the output will be 'YES', followed by 2, then `n - k + 1`, and finally 1.
    #- Otherwise, the output will be 'NO'.
    #
    #The exact output depends on the specific values of `n` and `k` for each iteration, but it will consist of lines starting with 'YES' or 'NO', followed by either 1, 1 or 2, `n - k + 1`, and 1 (if applicable).
#Overall this is what the function does:The function processes up to 1000 test cases, each involving two positive integers \(n\) and \(k\). For each test case, it determines whether certain conditions are met and outputs a result accordingly. If \(n\) equals \(k\), it prints 'YES' followed by 1 and 1. If \(n + 2\) is greater than \(2k\), it prints 'YES' followed by 2, then \(n - k + 1\), and finally 1. Otherwise, it prints 'NO'. The function does not return any value but prints the results directly.

