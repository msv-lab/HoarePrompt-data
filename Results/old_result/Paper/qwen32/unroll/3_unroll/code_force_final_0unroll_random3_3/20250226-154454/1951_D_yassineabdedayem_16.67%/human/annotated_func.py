#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 1 <= n, k <= 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        rep = 0
        
        number = 0
        
        tab = []
        
        while n != 0 and k > 0 and rep < 60 and n >= k:
            Min, Max = min(n // k, k), max(int(n / k), k)
            if Max == k and n * Min <= k:
                number = Min
                k = k - Max
            else:
                number = Max
                k = k - Min
            tab.append(str(number))
            n -= Min * Max
            rep += 1
        
        if k == 0:
            print('YES')
            print(len(tab))
            for i in tab:
                print(i, end=' ')
        else:
            print('NO')
        
    #State: For each test case, if `k` is reduced to zero, the output will be 'YES', followed by the length of the sequence `tab` and the sequence itself. If `k` is not reduced to zero, the output will be 'NO'.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it performs a series of operations to determine if `k` can be reduced to zero by subtracting products of pairs of numbers derived from `n` and `k`. If `k` is reduced to zero, it outputs 'YES', followed by the number of operations performed and the sequence of numbers used in the operations. If `k` cannot be reduced to zero, it outputs 'NO'.

