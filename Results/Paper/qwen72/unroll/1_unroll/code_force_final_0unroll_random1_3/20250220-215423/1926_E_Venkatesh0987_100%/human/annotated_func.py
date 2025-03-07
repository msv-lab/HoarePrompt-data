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
        
    #State: The loop iterates through each test case, and for each test case, it prints a value based on the conditions provided. The variables `n`, `k`, `s`, `i`, `d`, `h`, `p`, and `g` are modified within the loop, but their final values after the loop execution are not retained for the next iteration. Therefore, the initial state of `t` remains unchanged, and the values of `n` and `k` for the next test case are read from input.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k` (where 1 ≤ k ≤ n ≤ 10^9). For each test case, it calculates and prints a specific value based on the relationship between `n` and `k`. If `k` is greater than `(n + 1) // 2`, the function performs a series of calculations and prints a value derived from these calculations. Otherwise, it simply prints `2 * k - 1`. The function reads the number of test cases `t` (1 ≤ t ≤ 5 · 10^4) and processes each test case independently, with the state of variables reset for each new test case. After processing all test cases, the function does not return any value, but the results are printed to the console.

