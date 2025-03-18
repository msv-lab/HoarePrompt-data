#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: `t` is 0, `n` is 0, `k` is an input integer, `s` is the sum of the values of `(n + 1) // 2` from each iteration until `n` becomes 0, `m` is the highest power of 2 that divides the initial `n` without remainder, `x` is the last value of `(n + 1) // 2` before `n` became 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, where 1 ≤ t ≤ 5 · 10^4. For each test case, it reads two integers `n` and `k` from the input, where 1 ≤ k ≤ n ≤ 10^9. The function calculates and prints a value for each test case based on the relationship between `n` and `k`. After processing all test cases, the function concludes, and the state of the program is such that `t` is 0, `n` is 0, `k` is the last input integer for the final test case, `s` is the sum of the values of `(n + 1) // 2` from each iteration until `n` becomes 0, and `m` is the highest power of 2 that divides the initial `n` without remainder.

