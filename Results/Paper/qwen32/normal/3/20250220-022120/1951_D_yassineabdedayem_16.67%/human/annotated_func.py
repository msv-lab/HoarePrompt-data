#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 1 <= n, k <= 10^18.
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
        
    #State: If `k` is 0 after all iterations, the output will be "YES", followed by the length of `tab` and the elements of `tab`. If `k` is not 0, the output will be "NO".
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it determines whether it's possible to reduce `k` to 0 by repeatedly subtracting the minimum of `n // k` and `k` (or the maximum of `n // k` and `k` under certain conditions) from `k`, while also decrementing `n` accordingly. If `k` can be reduced to 0, it outputs "YES", followed by the number of operations performed and the sequence of numbers used in the operations. If `k` cannot be reduced to 0, it outputs "NO".

