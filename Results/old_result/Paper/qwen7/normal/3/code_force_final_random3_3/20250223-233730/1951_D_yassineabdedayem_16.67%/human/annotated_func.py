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
        
    #State: All variables except `t` will be reset to their initial states after the loop completes. `t` will be 0 since it was decremented by 1 each time the loop ran and there were no further inputs to increment it.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of three positive integers: t, n, and k. For each test case, it determines whether it is possible to reduce n to 0 by repeatedly subtracting a value derived from n and k, and prints 'YES' along with the number of operations performed if possible, or 'NO' otherwise. After processing all test cases, the function outputs no further information.

