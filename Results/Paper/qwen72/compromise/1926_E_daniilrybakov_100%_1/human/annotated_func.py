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
        
    #State: The loop has executed all iterations, and for each test case, the output is a calculated integer based on the input values of n and k. The values of t, n, and k are unchanged as they are input values, and the loop variables s and m are reset for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` (where 1 ≤ k ≤ n ≤ 10^9). The function calculates and prints an integer for each test case based on the values of `n` and `k`. After processing all test cases, the function has no return value, and the input variables `t`, `n`, and `k` remain unchanged. The loop variables `s` and `m` are reset for each test case.

