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
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: The loop executes for each test case, and for each test case, it prints a value based on the conditions provided. The variables `n`, `k`, `s`, `i`, `d`, `h`, `p`, and `g` are updated within the loop, but they are reinitialized for each test case. After the loop finishes executing all the iterations, the values of `n` and `k` for each test case will be the same as they were initially, and the values of `s`, `i`, `d`, `h`, `p`, and `g` will be reset to their initial values for the next test case. The output for each test case will be a single integer, either `2 * k - 1` or `2
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` representing the number of test cases, and for each test case, it accepts two integers `n` and `k` such that 1 ≤ k ≤ n ≤ 10^9. For each test case, the function calculates and prints a single integer result. If `k` is greater than `(n + 1) // 2`, the function performs a series of calculations and prints a value derived from these calculations. Otherwise, it prints `2 * k - 1`. After processing all test cases, the function has no side effects on the input variables `n` and `k`, and all local variables are reset for the next test case.

