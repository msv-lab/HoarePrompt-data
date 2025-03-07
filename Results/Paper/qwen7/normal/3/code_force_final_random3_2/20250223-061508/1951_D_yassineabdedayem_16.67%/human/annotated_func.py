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
        
    #State: `rep` is 60, `n` is 0, `k` is 0, `Min` is 0, `Max` is 0, `number` is the last value appended to `tab` during the 60th iteration, and `tab` is a list containing the string representations of numbers from 0 to 59 inclusive.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, n, and k. For each test case, it determines whether n can be reduced to 0 by repeatedly subtracting multiples of k from n, while keeping track of the operations performed. If n can be reduced to 0, it prints 'YES' followed by the number of operations and the sequence of operations. Otherwise, it prints 'NO'. The function returns no direct output but modifies the standard output based on the given inputs.

