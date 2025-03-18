#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}. The function will be called multiple times with different values of n and k, up to 1000 times in total.
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
        
    #State: After all iterations, `t` will be 0, and the values of `n` and `k` will be the last pair of integers read from the input. The program will have printed the appropriate output for each pair of `n` and `k` as per the given conditions.
#Overall this is what the function does:The function reads multiple pairs of positive integers `n` and `k` from the input, and for each pair, it determines whether it is possible to partition `n` into `k` parts under specific conditions. If it is possible, it prints 'YES' followed by the number of parts and their sizes; otherwise, it prints 'NO'.

