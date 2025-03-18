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
        
    #State: After the loop executes all the iterations, `t` is 0, and for each test case, `n` and `k` are the final values after the loop's operations, `rep` is the number of iterations performed (up to 60), `number` is the last value appended to `tab`, and `tab` is a list of strings representing the numbers generated during the loop. If `k` is 0, the loop prints 'YES', the length of `tab`, and the contents of `tab`. If `k` is not 0, the loop prints 'NO'.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two positive integers `n` and `k` from the standard input. It then performs a series of operations to generate a list of numbers and checks if `k` can be reduced to 0. If `k` is 0 after the operations, the function prints 'YES', the length of the list, and the list itself. If `k` is not 0, the function prints 'NO'. The function does not return any values; it only prints the results to the standard output.

