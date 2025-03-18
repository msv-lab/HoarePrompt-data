#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
        
    #State: The loop has executed `t` times, and for each iteration, the program has read two integers `n` and `k`. Depending on the values of `n` and `k`, the program has printed either "YES" followed by two integers, or "NO". The conditions for printing "YES" and the specific integers printed remain the same as described in the initial states. The variables `n` and `k` are updated with new values from the input at the start of each iteration, and `t` is a positive integer representing the total number of iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`. It then determines if it's possible to partition `n` into `k` parts under certain conditions and prints "YES" followed by the number of parts and their sizes if possible, or "NO" if not.

