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
        
    #State: The loop iterates `t` times. For each iteration, the values of `n` and `k` are read from input. The loop modifies `n`, `k`, `rep`, `number`, and `tab` within the while loop. After the while loop, `n` is reduced to a value that is either 0 or less than `k`, `k` is reduced to a non-positive value or remains positive if `n` is less than `k`, `rep` is incremented up to 60, `number` holds the last value appended to `tab`, and `tab` contains a list of strings representing the values of `number` appended during the loop. If `k` is 0, the loop prints 'YES', the length of `tab`, and the elements of `tab`. If `k` is not 0, the loop prints 'NO'. The variables `n`, `k`, `rep`, `number`, and `tab` are reset for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18). For each test case, it attempts to reduce `n` by repeatedly subtracting the product of the minimum and maximum of `n // k` and `k` from `n`, while also decrementing `k` by the minimum of these two values. This process is repeated up to 60 times or until `n` is less than `k` or `k` becomes non-positive. If `k` reaches 0, the function prints 'YES', the number of operations performed, and the sequence of numbers representing the operations. If `k` is still positive after the process, the function prints 'NO'. The function does not return any values; it only prints the results to the console.

