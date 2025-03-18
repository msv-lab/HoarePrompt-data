#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, n and k are positive integers such that 1 <= n, k <= 10^{18}.
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
        
    #State: t is 0; n, k, rep, tab, and number are determined by the input values for each iteration. If k is 0 for any iteration, it prints 'YES', the length of tab, and the elements of tab; otherwise, it prints 'NO'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers `n` and `k`. For each test case, it attempts to reduce `k` to zero by repeatedly subtracting the product of two derived values from `n`. If `k` is reduced to zero, it outputs 'YES', the number of steps taken, and the sequence of values used in the reduction. If `k` cannot be reduced to zero, it outputs 'NO'.

