#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers where 1 ≤ n, k ≤ 10^18.
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
        
    #State: `t` is 0, `n` is 0 or a non-negative integer, `k` is 0 or a positive integer, `rep` is the total number of times the loop executed (which is at most 60), `tab` is a list containing the string representations of the `number` values computed during each iteration of the loop. If `k` is 0, `tab` contains at least `rep` elements, and the elements of `tab` have been printed. If `k` is a positive integer, `tab` contains the string representations of the `number` values computed during each iteration of the loop, and the loop has stopped because one of the conditions `n != 0`, `k > 0`, or `rep < 60` is no longer true.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by two positive integers `n` and `k` (where 1 ≤ n, k ≤ 10^18). For each test case, it attempts to decompose `n` into a sum of products of two integers, where one integer is at most `k` and the other is a divisor of `n`. The function records these products in a list `tab` and stops after 60 iterations or when `n` cannot be further decomposed under the given constraints. If `k` is reduced to 0, the function prints "YES" followed by the number of elements in `tab` and the elements themselves. If `k` is not 0, the function prints "NO". After processing all test cases, `t` is 0, `n` is 0 or a non-negative integer, `k` is 0 or a positive integer, and `rep` is the total number of times the loop executed (at most 60).

