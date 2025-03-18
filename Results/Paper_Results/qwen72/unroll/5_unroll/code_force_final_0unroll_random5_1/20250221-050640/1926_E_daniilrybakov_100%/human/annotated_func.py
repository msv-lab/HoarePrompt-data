#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: The loop will print a series of integers, one for each iteration, based on the input values of `n` and `k`. The variables `t`, `n`, and `k` will retain their initial values, while the variables `s` and `m` will be reset to 0 and 1, respectively, at the start of each iteration. After the loop finishes all iterations, `t` will be unchanged, and `n` and `k` will retain their last input values.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 50,000`. It then performs `t` iterations, each time reading two integers `n` and `k` from the input, where `1 ≤ k ≤ n ≤ 1,000,000,000`. For each pair of `n` and `k`, the function calculates and prints an integer value. The variables `t`, `n`, and `k` retain their initial values after the function completes, and the function does not return any value.

