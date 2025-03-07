#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
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
        
    #State: t is an input integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18. After the loop, t is decremented by the number of test cases processed, and for each test case, n is reduced by the sum of products of Min and Max calculated in each iteration, and k is reduced by the sum of Min and Max values used in each iteration. The loop will print 'YES' followed by the length of the tab list and the elements of tab if k is reduced to 0, otherwise it will print 'NO'.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is defined by two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18). It attempts to reduce `n` by repeatedly subtracting the product of the minimum and maximum of `n // k` and `k` until `n` is less than `k` or a maximum of 60 iterations is reached. If `k` is reduced to 0 within these constraints, the function prints 'YES', the number of iterations performed, and the sequence of numbers used in the reduction. Otherwise, it prints 'NO'. The function processes up to 1000 test cases. After processing all test cases, the function exits without returning any value.

