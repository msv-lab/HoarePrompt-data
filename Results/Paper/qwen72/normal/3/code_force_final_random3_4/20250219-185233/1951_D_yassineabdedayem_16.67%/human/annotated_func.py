#State of the program right berfore the function call: t is an integer such that 1 \le t \le 1000, and for each test case, n and k are positive integers such that 1 \le n, k \le 10^{18}.
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
        
    #State: `t` is 0, `n` and `k` are the final values after all iterations of the loop, `rep` is 60 or less, `tab` is a list containing string representations of `number` for each iteration, `i` is `None` (since `k` is 0 or the loop condition is no longer satisfied), `Min` and `Max` are the last computed minimum and maximum values of `n // k` and `k` respectively, and `number` is the last value assigned to it during the loop. If `k` is 0, `i` is the last element of `tab` (or `None` if `tab` is empty), and `tab` has been fully iterated. If `k` is a positive integer, `i` is `None`.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` indicating the number of test cases. For each test case, it reads two positive integers `n` and `k`. The function then attempts to decompose `n` into a sum of products of integers, where each product is formed by a pair of integers whose values are determined by the current values of `n` and `k`. The function keeps track of these products in a list `tab`. If it successfully decomposes `n` such that `k` becomes 0, it prints 'YES', the length of `tab`, and the elements of `tab`. If it cannot decompose `n` to make `k` 0, it prints 'NO'. After processing all test cases, `t` is 0, and the state of `n`, `k`, `rep`, `tab`, `Min`, `Max`, and `number` is undefined for the next test case.

