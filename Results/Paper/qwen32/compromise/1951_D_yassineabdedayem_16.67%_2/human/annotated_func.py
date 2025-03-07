#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t lines contains two positive integers n and k such that 1 <= n, k <= 10^{18}.
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
        
    #State: t is 0; n and k are the values from the last test case; rep is the number of iterations for the last test case; tab is the list of numbers for the last test case if k was 0; Min and Max are the last computed values for the last test case; number is the last computed value for the last test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two positive integers `n` and `k`. For each test case, it determines if it's possible to reduce `n` to zero by repeatedly subtracting the product of two numbers, where one number is the minimum of `n // k` and `k`, and the other is the maximum of `n // k` and `k`. If `n` can be reduced to zero, it outputs "YES" followed by the number of operations performed and the sequence of numbers used in the operations. If `n` cannot be reduced to zero, it outputs "NO".

