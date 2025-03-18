#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
        
    #State: All variables outside the loop, such as `t`, `n`, `k`, `rep`, `number`, `tab`, `Min`, and `Max`, will retain their values from the final iteration. Specifically, `t` will be the initial value, `n` will be 0, `k` will be 0, `rep` will be 60, `number` will be 0, `tab` will be an empty list, `Min` will be 0, and `Max` will be 0.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of three values: t (the number of iterations), n (a positive integer), and k (another positive integer). For each test case, it determines whether n can be reduced to zero by repeatedly subtracting multiples of k, and prints 'YES' along with the number of operations performed if possible, or 'NO' otherwise. After processing all test cases, it outputs the final state of the program, which includes the initial value of t, n set to 0, k set to 0, rep set to 60, number set to 0, tab as an empty list, and both Min and Max set to 0.

