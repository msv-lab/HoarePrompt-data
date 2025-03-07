#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4, and for each of the t test cases, n and k are integers such that 1 <= k <= n <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: After processing all test cases, the variables `n`, `k`, `L`, `tot`, and `pow` will hold the values from the last test case processed. Specifically, `n` will be 0, `k` will be the `k` value from the last test case, `L` will be the list constructed for the last test case, `tot` will be the total sum of elements in `L` for the last test case, and `pow` will be 2 raised to the power of the number of elements in `L` for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it calculates and prints a specific value based on the relationship between `n` and `k`.

