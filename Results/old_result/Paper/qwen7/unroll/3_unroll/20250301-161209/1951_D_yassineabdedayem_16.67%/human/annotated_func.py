#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
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
        
    #State: Output State: The value of `t` integers are processed according to the given loop. For each integer `n` and `k`, if it's possible to repeatedly subtract multiples of `k` from `n` until `n` becomes less than `k` or `rep` (the number of iterations) reaches 60, then "YES" is printed followed by the length of the list `tab` and the elements of `tab`. Otherwise, "NO" is printed. Here, `tab` contains the sequence of numbers chosen during each iteration.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it takes two integers \( n \) and \( k \) and determines whether it is possible to repeatedly subtract multiples of \( k \) from \( n \) until \( n \) becomes less than \( k \) or a maximum of 60 iterations have been performed. If this condition is met, it prints "YES" followed by the count of iterations and the sequence of numbers used in each iteration. Otherwise, it prints "NO". The function implicitly accepts the number of test cases \( t \) as input and does not return any value but outputs the results for each test case.

