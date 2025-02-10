#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * f
            print(y)
        else:
            print(2 * k - 1)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5 · 10^4, `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 10^9, `n` and `k` are the values read from the input. For each test case, if `k` > `(n + 1) // 2`, then `s` is equal to `k`, `d` is 0, `h` is 0, `p` is `i`, `g` is the sum of the series of `(h + 1) // 2` for each iteration, `f` is `k - g`, and `y` is 2. Otherwise, if `k` ≤ `(n + 1) // 2`, then `s` is 0, `d` is `n`, `h` is `n`, `p` is 1, `g` is 0, `f` is undefined, `y` is undefined, and `i` is 0.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k` where `1 ≤ k ≤ n ≤ 10^9`. For each test case, if `k` is greater than `(n + 1) // 2`, the function calculates a value `y` using a specific algorithm and prints it. If `k` is less than or equal to `(n + 1) // 2`, the function prints `2 * k - 1`. The function does not return any value; it only prints the results for each test case.

