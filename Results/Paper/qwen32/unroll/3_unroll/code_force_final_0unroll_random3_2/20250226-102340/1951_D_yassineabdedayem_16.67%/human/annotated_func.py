#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 1 <= n, k <= 10^{18}.
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
        
    #State: For each test case, the output will be either 'YES' followed by the length of the list `tab` and the elements of `tab`, or 'NO'. The variables `t`, `n`, `k`, `rep`, `number`, and `tab` will be in a state determined by the execution of the loop for that test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it determines if it's possible to reduce `n` to zero by repeatedly subtracting products of two integers derived from `n` and `k`, while keeping track of the number of such operations. If `n` can be reduced to zero within the constraints, it outputs 'YES' followed by the count of operations and the sequence of integers used. Otherwise, it outputs 'NO'.

