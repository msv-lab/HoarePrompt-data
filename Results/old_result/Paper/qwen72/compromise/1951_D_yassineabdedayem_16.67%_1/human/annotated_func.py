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
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 1000, `_` is `t - 1`, `n` is the remaining value after all iterations of the loop, `k` is the remaining value after all iterations of the loop, `rep` is the total number of iterations (up to 60) for the last test case, `tab` is a list containing the string representations of the `number` values generated during each iteration for the last test case, and `number` is the last value of `number` generated in the loop for the last test case. If `k` is 0, the program prints 'YES', the length of `tab`, and all elements in `tab` separated by spaces. Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 1000`, representing the number of test cases. For each test case, it reads two positive integers `n` and `k` from the input, where `1 ≤ n, k ≤ 10^18`. The function then performs a series of operations to determine if it is possible to reduce `n` to 0 by repeatedly subtracting the product of `Min` and `Max` from `n`, where `Min` and `Max` are the minimum and maximum of `n // k` and `k`, respectively. If `k` reaches 0 before `n` becomes 0, the function prints 'YES', followed by the number of operations performed and the sequence of numbers used in the operations. If `k` does not reach 0, the function prints 'NO'. After processing all test cases, the function concludes, and the final state includes the remaining values of `n` and `k` for the last test case, the total number of iterations `rep` (up to 60), and the list `tab` containing the string representations of the numbers used in the operations for the last test case.

