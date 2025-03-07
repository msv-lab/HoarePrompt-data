#State of the program right berfore the function call: Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^{18}) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. There are multiple test cases, with the first line containing an integer t (1 ≤ t ≤ 1000) indicating the number of test cases.
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
        
    #State: `t` remains unchanged, `n` and `k` are reset for each test case, `rep` is 0, `number` is undefined, `tab` is an empty list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `n` and `k`. It determines whether Alice can buy exactly `k` jewels using her `n` coins, and for each test case, it outputs "YES" along with the number of transactions and the details of each transaction if possible, or "NO" if it is not possible to buy exactly `k` jewels.

